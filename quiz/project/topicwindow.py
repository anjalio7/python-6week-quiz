from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.ttk import Combobox
import database

class Labelwindow:
  def __init__(self): 
        
    self.root=Toplevel()
    self.root.title(' QUIZ HUB')
    self.root.resizable(FALSE,FALSE)
    self.root.geometry('700x600+400+100')
    
 
    # show image
    self.Image= ImageTk.PhotoImage(Image.open('2..jpeg').resize((700,600)))
    self.label1 = Label(self.root, image = self.Image)
    self.label1.place(x=0,y=-5)
    
    # show the text in window
    Label(self.root, text="Add Topic ",font="none 50 italic ",fg='white',bg="black").place(x=200, y=130)
    Label(self.root, text="subject :",font= "calibri 31" ,fg='white',bg="black").place(x=140, y=250)
    Label(self.root, text="topic :",font= " calibri   31" ,fg='white',bg="black").place(x=180, y=300)
    
    self.entry1=Entry(self.root,bd=4,width=30,text='white',fg="black",font="Impact 8")  # use create box to fill details
    self.entry1.place(x=300,y=320)
    
    Button(self.root,text="ADD",bg="orange",bd=3,fg="black",width=5,font="italic 15", command=self.topic).place(x=280,y=400)
    
    # show use box for entry
  def comboWidget(self):
      self.dropValue = StringVar()
      self.options = database.allSubject()
      self.drop_Down = Combobox(self.root, textvariable=self.dropValue, values= self.options,font="none 11 italic")
      self.drop_Down.place(x=300,y=266)
        
      self.root.mainloop()

  def topic(self):
    if self.drop_Down.get() == '':
      messagebox.showerror('Error', 'Please select subject first.')
    elif self.entry1.get() == '':
      messagebox.showerror('Error', 'Please enter topic first.')
    else:
      a = list(self.drop_Down.get().split())
      self.data = (
        a[0],
        self.entry1.get()
      )

      res = database.addTopic(self.data)
      if res:
        messagebox.showinfo('Success', 'Topic added successfully.')
        self.root.destroy()
      else:
        messagebox.showerror('Error', 'Something went wrong.')



    
if __name__=="__main__":
    obj= Labelwindow()
    obj.comboWidget()