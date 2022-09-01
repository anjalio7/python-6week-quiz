from tkinter import *
from tkinter.ttk import Treeview
import userDatabase

class Labelwindow:
  def __init__(self, userRes):

    self.userRes = userRes

    self.root=Toplevel()
    self.root.title(' QUIZ HUB ')
    self.root.resizable(FALSE,FALSE)
    self.root.geometry('700x600+400+100')

    self.fr = Frame(self.root, bg="white")
    self.fr.place(x=0, y=0, width="800", height="500")

    self.tr = Treeview(self.fr, columns=('A', 'B', 'C', 'D' ),selectmode="extended")
     
    self.tr.heading('#0',text="ID")
    self.tr.column('#0',minwidth=2,width=70,stretch=NO)

    self.tr.heading('#1',text="Subject")
    self.tr.column('#1',minwidth=3,width=80,stretch=NO)

    self.tr.heading('#2',text="Topic")
    self.tr.column('#2',minwidth=4,width=90 ,stretch=NO)

    self.tr.heading('#3',text="T. Question")
    self.tr.column('#3',minwidth=4,width=90 ,stretch=NO)

    self.tr.heading('#4',text="Score")
    self.tr.column('#4',minwidth=4,width=90 ,stretch=NO)

    res = userDatabase.fetchScore(self.userRes)
    if res:
        for i in res:
            self.tr.insert('', 0, text = i[0], values=(i[1], i[2], i[4],i[3]))
    
    self.tr.place(x=0,y=0,width="800",height="500")

    self.root.mainloop()
        

if __name__ == '__main__':
    obj = Labelwindow()