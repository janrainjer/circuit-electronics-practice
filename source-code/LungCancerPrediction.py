def calculate(ge, ag, sm, yf, an, pe, ch, fa, al, wh, alc, co, sh, sw, cp):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
    from sklearn.preprocessing import LabelEncoder
    import warnings
    from imblearn.over_sampling import RandomOverSampler
    from sklearn.model_selection import RandomizedSearchCV, train_test_split
    from sklearn.preprocessing import StandardScaler

    plt.style.use('fivethirtyeight')
    colors = ['#011f4b', '#03396c', '#005b96', '#6497b1', '#b3cde0']
    sns.set_palette(sns.color_palette(colors))

    df = pd.read_csv('data/survey_lung_cancer.csv')

    df.drop_duplicates(inplace=True)

    # Encoding LUNG_CANCER and GENDER column
    encoder = LabelEncoder()
    df['LUNG_CANCER'] = encoder.fit_transform(df['LUNG_CANCER'])
    df['GENDER'] = encoder.fit_transform(df['GENDER'])
    # print(df.head(15))

    # Separating continuous and categorical columns
    con_col = ['AGE']
    cat_col = []
    for i in df.columns:
        if i != 'AGE':
            cat_col.append(i)

    # Visualizing AGE columns

    warnings.filterwarnings('ignore')
    # fig,ax = plt.subplots(1,3,figsize=(20,6))
    # sns.distplot(df['AGE'],ax=ax[0])
    # sns.histplot(data =df,x='AGE',ax=ax[1],hue='LUNG_CANCER',kde=True)
    # sns.boxplot(x=df['LUNG_CANCER'],y=df['AGE'],ax=ax[2])
    # plt.suptitle("Visualizing AGE column",size=20)
    # # plt.show()

    # Heat map (Pearson's Similarity)
    # plt.figure(figsize=(15,15))
    # sns.heatmap(df.corr(),annot=True,linewidth=0.5,fmt='0.2f')
    # plt.show()

    # Data Preprocessing

    # Separating Independent and Dependent Feature
    X = df.drop(['LUNG_CANCER'], axis=1)
    y = df['LUNG_CANCER']

    # Changing values of columns from 2,1 to 1,0 (2/1 to 1/0 in each data)
    for i in X.columns[2:]:
        temp = []
        for j in X[i]:
            temp.append(j-1)
        X[i] = temp
    # print(X.head()) # Debug

    # Oversampling of Minority Class
    X_over, y_over = RandomOverSampler().fit_resample(X, y)

    # Train Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X_over, y_over, random_state=42, stratify=y_over)
    # print(f'Train shape : {X_train.shape}\nTest shape: {X_test.shape}')

    # Scaling of AGE column
    scaler = StandardScaler()
    X_train['AGE'] = scaler.fit_transform(X_train[['AGE']])
    X_test['AGE'] = scaler.transform(X_test[['AGE']])
    X_train.head()

    # Model Building
    # Logistic Regression
    param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100],
                  'max_iter': [50, 75, 100, 200, 300, 400, 500, 700]}
    log = RandomizedSearchCV(LogisticRegression(
        solver='lbfgs'), param_grid, cv=5)
    log.fit(X_train, y_train)
    y_pred_log = log.predict(X_test)
    confusion_log = confusion_matrix(y_test, log.predict(X_test))
    plt.figure(figsize=(8, 8))
    sns.heatmap(confusion_log, annot=True)
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    # plt.show()
    print(classification_report(y_test, y_pred_log))

    # Accuracy Score
    acc = accuracy_score(y_test, y_pred_log)
    print(acc)

    # User input
    new_input = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    new_input[0][0] = ge
    new_input[0][1] = ag
    new_input[0][2] = sm
    new_input[0][3] = yf
    new_input[0][4] = an
    new_input[0][5] = pe
    new_input[0][6] = ch
    new_input[0][7] = fa
    new_input[0][8] = al
    new_input[0][9] = wh
    new_input[0][10] = alc
    new_input[0][11] = co
    new_input[0][12] = sh
    new_input[0][13] = sw
    new_input[0][14] = cp

    new_input[0][1] = scaler.fit_transform([[60]])

    new_output = log.predict(new_input)
    print("Predicted :", 'YES' if new_output[0] == 1 else 'NO')
    if new_output[0] == 1:
        return 1
    else:
        return 0
