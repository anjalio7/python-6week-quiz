
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import database

class Labelwindow:
  def __init__(self):  
    self.root=Toplevel()
    self.root.title(' QUIZ HUB ')
    self.root.resizable(FALSE,FALSE)
    self.root.geometry('700x600+400+100')
    
    # show image
    self.Image= ImageTk.PhotoImage(Image.open('2..jpeg').resize((700,600)))
    self.label1 = Label(self.root, image = self.Image)
    self.label1.place(x=0,y=-5)
   # Frame(self.root,bg="white",bd=40).place(width=500,height=400,x=100,y=110)
    
    # show the text in window
    Label(self.root, text="Add subject ",font="none 40 italic ",fg='white',bg="black").place(x=200, y=130)
    Label(self.root, text="subject :",font= "calibri 31" ,fg='white',bg="black").place(x=150, y=250)
    
    # show use box for entry
    self.entry1=Entry(self.root,bd=4,width=30,text='black',fg="black",font="Impact 10" )  # use create box to fill details
    self.entry1.place(x=300,y=266)
    
    ##Button
    Button(self.root,text="ADD",bg="orange",bd=3,fg="black",width=5,font="italic 15", command=self.subject).place(x=280,y=360)
    self.root.mainloop()


  def subject(self):
    if self.entry1.get() == '':
      messagebox.showerror('Alert', 'Please enter subject')
    else:
      self.data = (
        self.entry1.get(),
      )
      res = database.addSubject(self.data)
      if res:
        messagebox.showinfo('Success', 'Subject added successfully')
        self.root.destroy()
      else:
        messagebox.showerror('Error', 'Something went wrong.')

if __name__=="__main__":
    obj= Labelwindow()