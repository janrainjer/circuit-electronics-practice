import tkinter as tk
import tkinter.font as tkFont
from LungCancerPrediction import *
from PIL import Image, ImageTk


class App:
    def __init__(self, root):
        # variable
        self.gender = tk.IntVar()
        self.age = tk.IntVar()
        self.smoke = tk.IntVar()
        self.yellow = tk.IntVar()
        self.anxiety = tk.IntVar()
        self.peer = tk.IntVar()
        self.chronic = tk.IntVar()
        self.fatigue = tk.IntVar()
        self.allergy = tk.IntVar()
        self.wheezing = tk.IntVar()
        self.alcohol = tk.IntVar()
        self.cough = tk.IntVar()
        self.shortB = tk.IntVar()
        self.swallow = tk.IntVar()
        self.chestP = tk.IntVar()
        self.txt = "No"
        # setting title
        root.title("LCP Application")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root['bg'] = "#ffffff"

        # Icon
        photo = ImageTk.PhotoImage(file="images/lung.png")
        root.iconphoto(False, photo)

        # Medical Image
        self.original = Image.open('images/medical.png')
        resized = self.original.resize((125, 125), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        self.display = tk.Label(root, image=self.image, bg="#ffffff")
        self.display.place(x=430, y=350)

        # Header
        tk.Label(root, font=tkFont.Font(family='Times', size=16), fg="#084a0f", bg="#ffffff",
                 justify="center", text="Lung Cancer Prediction Application").place(x=160, y=20, width=300, height=25)

        # Input
        tk.Label(root, font=tkFont.Font(family='Times', size=16), fg="#084a0f", bg="#ffffff",
                 justify="center", text="Input Your Data").place(x=40, y=60, width=150, height=25)

        # Gender
        tk.Radiobutton(root, font=tkFont.Font(family='Times', size=10), fg="#000000", bg='#ffffff', justify='center', text='Male',
                       variable=self.gender, value=1).place(x=30, y=110, width=85, height=25)
        tk.Radiobutton(root, font=tkFont.Font(family='Times', size=10), fg="#000000", bg='#ffffff', justify='center', text='Female',
                       variable=self.gender, value=0).place(x=115, y=110, width=85, height=25)
        tk.Label(root, font=tkFont.Font(family='Times', size=12), fg="#084a0f", bg="#ffffff",
                 justify="center", text="Gender").place(x=36, y=90, width=70, height=25)

        # Age
        tk.Label(root, font=tkFont.Font(family='Times', size=12), fg="#084a0f", bg="#ffffff",
                 justify="center", text="Age").place(x=250, y=90, width=70, height=25)
        self.AgeEntryBox = tk.Entry(root, bg="#8b8b8b", borderwidth="1px", font=tkFont.Font(family='Times', size=12),
                                    fg="#000000", justify="center", text="Entry")
        self.AgeEntryBox.place(x=270, y=110, width=70, height=25)

        # Smoking
        tk.Label(root, font=tkFont.Font(family='Times', size=12), fg="#084a0f", bg="#ffffff",
                 justify="center", text="Smoking").place(x=40, y=140, width=70, height=25)
        tk.Checkbutton(root, font=tkFont.Font(family='Times', size=12), fg="#000000", bg="#ffffff", justify="center",
                       text="Yes", variable=self.smoke, offvalue="0", onvalue="1").place(x=35, y=160, width=70, height=25)

        # Yellow Fingers
        tk.Label(root, font=tkFont.Font(family='Times', size=12), fg="#084a0f", bg="#ffffff",
                 justify="center", text="Yellow Fingers").place(x=33, y=190, width=120, height=25)
        tk.Checkbutton(root, font=tkFont.Font(family='Times', size=12), fg="#000000", bg="#ffffff", justify="center",
                       text="Yes", variable=self.yellow, offvalue="0", onvalue="1").place(x=35, y=210, width=70, height=25)

        # Anxiety
        tk.Label(root, font=tkFont.Font(family='Times', size=12), fg="#084a0f", bg="#ffffff",
                 justify="center", text="Anxiety").place(x=36, y=237, width=70, height=25)
        tk.Checkbutton(root, font=tkFont.Font(family='Times', size=12), fg="#000000", bg="#ffffff", justify="center",
                       text="Yes", variable=self.anxiety, offvalue="0", onvalue="1").place(x=35, y=257, width=70, height=25)

        # Peer Pressure
        tk.Label(root, font=tkFont.Font(family='Times', size=12), fg="#084a0f", bg="#ffffff",
                 justify="center", text="Peer Pressure").place(x=30, y=285, width=120, height=25)
        tk.Checkbutton(root, font=tkFont.Font(family='Times', size=12), fg="#000000", bg="#ffffff", justify="center",
                       text="Yes", variable=self.peer, offvalue="0", onvalue="1").place(x=35, y=305, width=70, height=25)

        #  Chronic Disease
        tk.Label(root, font=tkFont.Font(family='Times', size=12), fg="#084a0f", bg="#ffffff",
                 justify="center", text="Chronic Disease").place(x=170, y=140, width=120, height=25)
        tk.Checkbutton(root, font=tkFont.Font(family='Times', size=12), fg="#000000", bg="#ffffff", justify="center",
                       text="Yes", variable=self.chronic, offvalue="0", onvalue="1").place(x=167, y=160, width=70, height=25)

        # Fatigue
        tk.Label(root, font=tkFont.Font(family='Times', size=12), fg="#084a0f", bg="#ffffff",
                 justify="center", text="Fatigue").place(x=167, y=190, width=70, height=25)
        tk.Checkbutton(root, font=tkFont.Font(family='Times', size=12), fg="#000000", bg="#ffffff", justify="center",
                       text="Yes", variable=self.fatigue, offvalue="0", onvalue="1").place(x=167, y=210, width=70, height=25)

        # Allergy
        tk.Label(root, font=tkFont.Font(family='Times', size=12), fg="#084a0f", bg="#ffffff",
                 justify="center", text="Allergy").place(x=166.5, y=237, width=70, height=25)
        tk.Checkbutton(root, font=tkFont.Font(family='Times', size=12), fg="#000000", bg="#ffffff", justify="center",
                       text="Yes", variable=self.allergy, offvalue="0", onvalue="1").place(x=167, y=257, width=70, height=25)

        # Wheezing
        tk.Label(root, font=tkFont.Font(family='Times', size=12), fg="#084a0f", bg="#ffffff",
                 justify="center", text="Wheezing").place(x=173, y=285, width=70, height=25)
        tk.Checkbutton(root, font=tkFont.Font(family='Times', size=12), fg="#000000", bg="#ffffff", justify="center",
                       text="Yes", variable=self.wheezing, offvalue="0", onvalue="1").place(x=167, y=305, width=70, height=25)

        # Alcohol Consuming
        tk.Label(root, font=tkFont.Font(family='Times', size=12), fg="#084a0f", bg="#ffffff",
                 justify="center", text="Alcohol Consuming").place(x=320, y=140, width=140, height=25)
        tk.Checkbutton(root, font=tkFont.Font(family='Times', size=12), fg="#000000", bg="#ffffff", justify="center",
                       text="Yes", variable=self.alcohol, offvalue="0", onvalue="1").place(x=317, y=160, width=70, height=25)

        # Coughing
        tk.Label(root, font=tkFont.Font(family='Times', size=12), fg="#084a0f", bg="#ffffff",
                 justify="center", text="Coughing").place(x=324, y=190, width=70, height=25)
        tk.Checkbutton(root, font=tkFont.Font(family='Times', size=12), fg="#000000", bg="#ffffff", justify="center",
                       text="Yes", variable=self.cough, offvalue="0", onvalue="1").place(x=317, y=210, width=70, height=25)

        # Shortness of Breath
        tk.Label(root, font=tkFont.Font(family='Times', size=12), fg="#084a0f", bg="#ffffff",
                 justify="center", text="Shortness of Breath").place(x=315, y=237, width=150, height=25)
        tk.Checkbutton(root, font=tkFont.Font(family='Times', size=12), fg="#000000", bg="#ffffff", justify="center",
                       text="Yes", variable=self.shortB, offvalue="0", onvalue="1").place(x=317, y=257, width=70, height=25)

        # Swallowing Difficulty
        tk.Label(root, font=tkFont.Font(family='Times', size=12), fg="#084a0f", bg="#ffffff",
                 justify="center", text="Swallowing Difficulty").place(x=318, y=285, width=150, height=25)
        tk.Checkbutton(root, font=tkFont.Font(family='Times', size=12), fg="#000000", bg="#ffffff", justify="center",
                       text="Yes", variable=self.swallow, offvalue="0", onvalue="1").place(x=317, y=307, width=70, height=25)

        # Chest Pain
        tk.Label(root, font=tkFont.Font(family='Times', size=12), fg="#084a0f", bg="#ffffff",
                 justify="center", text="Chest Pain").place(x=30, y=330, width=100, height=25)
        tk.Checkbutton(root, font=tkFont.Font(family='Times', size=12), fg="#000000", bg="#ffffff", justify="center",
                       text="Yes", variable=self.chestP, offvalue="0", onvalue="1").place(x=35, y=350, width=70, height=25)

        # Predict Button
        tk.Button(root, font=tkFont.Font(family='Times', size=12), bg="#ffffff", fg="#132bb0", justify="center",
                  text="Predict", command=self.PredictButton_command).place(x=170, y=345, width=70, height=25)

        # Show Output
        self.OutputMessage = tk.Label(root, font=tkFont.Font(family='Times', size=12), bg="#ffffff", fg="#b02613",
                                      justify="left", text="Lung Cancer : ")
        self.OutputMessage.place(x=60, y=370, width=200, height=100)

    # Predict
    def PredictButton_command(self):
        n = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        n[0][0] = self.gender.get()
        n[0][1] = self.AgeEntryBox.get()
        n[0][2] = self.smoke.get()
        n[0][3] = self.yellow.get()
        n[0][4] = self.anxiety.get()
        n[0][5] = self.peer.get()
        n[0][6] = self.chronic.get()
        n[0][7] = self.fatigue.get()
        n[0][8] = self.allergy.get()
        n[0][9] = self.wheezing.get()
        n[0][10] = self.alcohol.get()
        n[0][11] = self.cough.get()
        n[0][12] = self.shortB.get()
        n[0][13] = self.swallow.get()
        n[0][14] = self.chestP.get()

        result = calculate(n[0][0], n[0][1], n[0][2], n[0][3], n[0][4], n[0][5], n[0][6],
                           n[0][7], n[0][8], n[0][9], n[0][10], n[0][11], n[0][12], n[0][13], n[0][14])

        if result == 1:
            self.txt = "Lung Cancer : Yes"

        else:
            self.txt = "Lung Cancer : No"
        self.OutputMessage.config(text=self.txt)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
