
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox

from PIL import Image, ImageTk

import database
import json


class Labelwindow:
    def __init__(self, quesId):

        self.quesId = quesId

        self.root = Toplevel()
        self.root.title(' QUIZ HUB ')
        self.root.resizable(FALSE, FALSE)
        self.root.geometry('700x600+400+100')
        self.root.config(bg="black")

        self.image = ImageTk.PhotoImage(
            Image.open("2..jpeg").resize((700, 600)))
        self.label1 = Label(self.root, image=self.image)
        self.label1.place(x=0, y=-5)

        # show the text in window

        Label(self.root, text="subject :", font="calibri 15",
              fg='white', bg="black").place(x=70, y=90)
        Label(self.root, text="topic :", font=" calibri  15 ",
              fg='white', bg="black").place(x=85, y=120)
        Label(self.root, text="ADD QUESTION", font=" calibri  40 ",
              fg='white', bg="black").place(x=200, y=0)
        Label(self.root, text="Give options: ", font="calibri 25",
              fg='white', bg="black").place(x=75, y=220)
        Label(self.root, text="Q:", font=" calibri  30 ",
              fg='white', bg="black").place(x=65, y=170)

        #Label(self.root, text="A:",font= " calibri  20 " ,fg='white',bg="black").place(x=90, y=220)
        #Label(self.root, text="B:",font= " calibri  20 " ,fg='white',bg="black").place(x=90, y= 250)
        #Label(self.root, text="C:",font= " calibri  20 " ,fg='white',bg="black").place(x=90, y=280)
        #Label(self.root, text="D:",font= " calibri  20 " ,fg='white',bg="black").place(x=90, y=310)

        Label(self.root, text="Answer:", font=" calibri  20 ",
              fg='white', bg="black").place(x=90, y=390)

        # use create box to fill details
        self.quesEntry = Entry(self.root, bd=2, width=90)
        self.quesEntry.place(x=115, y=190)

        # use create box to fill details
        self.optEntry1 = Entry(self.root, bd=2, width=20)
        self.optEntry1.place(x=125, y=270)

        # use create box to fill details
        self.optEntry2 = Entry(self.root, bd=2, width=20)
        self.optEntry2.place(x=125, y=295)

        # use create box to fill details
        self.optEntry3 = Entry(self.root, bd=2, width=20)
        self.optEntry3.place(x=125, y=320)

        # use create box to fill details
        self.optEntry4 = Entry(self.root, bd=2, width=20)
        self.optEntry4.place(x=125, y=345)

        # use create box to fill details#alag hai
        self.ansEntry = Entry(self.root, bd=2, width=20)
        self.ansEntry.place(x=190, y=400)

        self.button = Button(self.root, text="ADD", bg="orange", bd=5, fg="black",
                             width=7, font="italic 11", command=self.addQues).place(x=300, y=480)

        # show use box for entry

    def comboWidget(self):
        # self.dropValue1 = StringVar()
        # self.options1 = database.allSubject()
        # self.drop_Downj = Combobox(
        #     self.root, textvariable=self.dropValue1, values=self.options1, font="none 8 italic")
        # self.drop_Downj.place(x=150, y=97)
        # self.drop_Downj.bind("<<ComboboxSelected>>", self.getTopics)

        self.options2 = database.allTopics()
        self.drop_Downy = Combobox(
            self.root, values=self.options2, font="none 8 italic")
        self.drop_Downy.place(x=150, y=125)

        res = database.singleQues(self.quesId)
        if res:
            a = []
            for i in range(len(res)):
                if i != 3:
                    a.append(res[i])
                else:
                    for k in json.loads(res[i]):
                        a.append(k)
            
            self.drop_Downy.insert(0, (a[0], a[1]))
            self.quesEntry.insert(0, a[2])
            self.optEntry1.insert(0, a[3])
            self.optEntry2.insert(0, a[4])
            self.optEntry3.insert(0, a[5])
            self.optEntry4.insert(0, a[6])
            self.ansEntry.insert(0, a[7])

        self.root.mainloop()

    def getTopics(self, e):
        a = list(self.drop_Downj.get().split())
        res = database.getTopic(a[0])
        if res:
            self.drop_Downy.config(state= 'normal')
            self.drop_Downy.config(values= res)
        else:
            messagebox.showerror('Alert', 'ssssssomething went wrong.')

    def addQues(self):
        if self.drop_Downy.get() == '':
            messagebox.showerror('Alert', 'select topic first')
        else:
            a = list(self.drop_Downy.get().split())
            self.data = (
                a[0],
              self.quesEntry.get(),
              json.dumps([self.optEntry1.get(), self.optEntry2.get(),
                         self.optEntry3.get(), self.optEntry4.get()]),
              self.ansEntry.get()
            )
            print(self.data)
            res = database.addQues(self.data)
            if res:
                messagebox.showinfo('Success', 'Question added successfully.')
                self.root.destroy()
            else:
                messagebox.showerror('Error', 'Something went wrong.')

if __name__ =="__main__":
    obj = Labelwindow()
    obj.comboWidget()
