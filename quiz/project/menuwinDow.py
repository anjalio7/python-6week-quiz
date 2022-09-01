
from tkinter import *
from PIL import Image,ImageTk
import question
import subject 
import topicwindow
import subList
import topicList, quesList, reports

class Labelwindow:
    def __init__(self):
        self.root = Tk()
        self.root.title('QUIZ HUB')
        self.root.geometry("700x600+400+100")
        self.root.resizable(width = False, height=False)
        self.frame=Frame(self.root,height=700,width=1400,bg="white")
        self.frame.place(x=0,y=0)
        
        self.image = ImageTk.PhotoImage(Image.open("7..jpeg").resize((700, 600)))
        self.label1 = Label(self.root, image = self.image)
        self.label1.place(x=0,y=-5)

    def menus(self):
        self.menubar = Menu(self.root)
        self.file = Menu(self.menubar)
        self.menubar.add_cascade(label="subject", menu=self.file)
        self.file.add_command(label="Add",command=self.openpage1)
        self.file.add_command(label = "Manage",command=self.openwindow3)
         
       
   
        # self.root.config(menu=self.menubar)
        self.file2 = Menu(self.menubar)
        self.menubar.add_cascade(label="Topic", menu=self.file2)
        self.file2.add_command(label="  Add ",command=self.openwindow )
        self.file2.add_command(label="Manage",command=self.openwindow4)
     
        # self.root.config(menu=self.menubar)
        self.file3 = Menu(self.menubar)
        self.menubar.add_cascade(label="Question", menu=self.file3)
        self.file3.add_command(label="  Add ",command=self.openwindow2 )
        self.file3.add_command(label="Manage", command=self.openQues)

        self.file4 = Menu(self.menubar)
        self.menubar.add_cascade(label='Reports', menu=self.file4)
        self.file4.add_command(label='View', command=self.openReports)

        self.root.config(menu=self.menubar)
        self.root.mainloop()
    def openpage1(self):
        #self.root.destroy()
        obj = subject.Labelwindow()
    
    def openwindow(self):
        #self.root.destroy()
        obj = topicwindow.Labelwindow()
        obj.comboWidget()
    def openwindow2(self):
       # self.root.destroy()
        obj=question.Labelwindow()
        obj.comboWidget()
    def openwindow3(self):
        obj = subList.Labelwindow()
    def openwindow4(self):
        obj = topicList.Labelwindow()
    
    def openQues(self):
        obj = quesList.Labelwindow()

    def openReports(self):
        obj = reports.Labelwindow()

if __name__ == "__main__":
    obj = Labelwindow()
    obj.menus()