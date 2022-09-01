
from tkinter import *
from PIL import Image,ImageTk
import selectSubject, scores

class Labelwindow:
    def __init__(self, userRes):

        self.userRes = userRes

        self.root = Tk()
        self.root.title('QUIZ HUB')
        self.root.geometry("700x600+400+100")
        self.root.resizable(width = False, height=False)
        self.frame=Frame(self.root,height=700,width=1400,bg="white")
        self.frame.place(x=0,y=0)
        
        # self.image = ImageTk.PhotoImage(Image.open("7..jpeg").resize((700, 600)))
        # self.label1 = Label(self.root, image = self.image)
        # self.label1.place(x=0,y=-5)

    def menus(self):
        self.menubar = Menu(self.root)
        self.file = Menu(self.menubar)
        self.menubar.add_cascade(label="Quiz", menu=self.file)
        self.file.add_command(label="Subject",command=self.openpage1)
         
       
   
        self.root.config(menu=self.menubar)
        self.file2 = Menu(self.menubar)
        self.menubar.add_cascade(label="Scores", menu=self.file2)
        self.file2.add_command(label="  View ",command=self.openwindow )
     
        self.root.config(menu=self.menubar)
        # self.file3 = Menu(self.menubar)
        # self.menubar.add_cascade(label="Question", menu=self.file3)
        # self.file3.add_command(label="  Add ",command=self.openwindow2 )
        # self.file3.add_command(label="Manage")
        # self.root.config(menu=self.menubar)
        self.root.mainloop()

    def openpage1(self):
        #self.root.destroy()
        obj = selectSubject.Labelwindow(self.userRes)
    
    def openwindow(self):
        #self.root.destroy()
        obj = scores.Labelwindow(self.userRes)
   

if __name__ == "__main__":
    obj = Labelwindow()
    obj.menus()