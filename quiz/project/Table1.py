from tkinter import *
from tkinter.ttk import Treeview
class Labelwindow:
  def __init__(self):  
    self.root=Toplevel()
    self.root.title(' QUIZ HUB ')
    self.root.resizable(FALSE,FALSE)
    self.root.geometry('700x600+400+100')

    self.fr = Frame(self.root, bg="white")
    self.fr.place(x=0, y=0, width="800", height="500")

    self.tr = Treeview(self.fr, columns=('A', 'B' ),selectmode="extended")
     
    self.tr.heading('#0',text="ID")
    self.tr.column('#0',minwidth=2,width=70,stretch=NO)

    self.tr.heading('#1',text="username")
    self.tr.column('#1',minwidth=3,width=80,stretch=NO)

    self.tr.heading('#2',text="password")
    self.tr.column('#2',minwidth=4,width=90 ,stretch=NO)
    
    self.tr.place(x=0,y=0,width="800",height="500")

    self.root.mainloop()
        

if __name__ == '__main__':
    obj = Labelwindow()