
from tkinter import*
from tkinter import messagebox  #use tu show enter your passowrd and your name etc.
from PIL import Image, ImageTk

import userDatabase, homeMenu

class Labelwindow:
    def __init__(self):
        self.root=Tk()  # create GUI
        self.root.title (" QUIZ HUB ")
        self.root.config(bg="black")
        self.root.geometry('700x600+400+100')
        # Show image using label
        # self.image = ImageTk.PhotoImage(Image.open('ra.png').resize((700, 600)))
        # self.label1 = Label(self.root, image = self.image)
        # self.label1.place(x=0,y=-5)
        
        #show quiz hub
        Label(self.root, text="Quiz Hub",font="none 60 italic ",fg='orange',bg="black",bd=0).place(x=85, y=30)
        
        # fetch imformation

        Label(self.root,text="username :",fg="white",bg="black",font="calibri 26 ").place(x=84,y=175)
        Label(self.root,text="password :",fg="white",bg="black",font="calibri 26 ").place(x=87,y=220)
        
        #entry_points
        self.entry1=Entry(self.root,bd=5,width=25)  # use create box to fill details
        self.entry1.place(x=250,y=190)
        self.entry2=Entry(self.root,bd=5,show="*",width=25)
        self.entry2.place(x=250,y=235)
        
        #Button
        Button(self.root,text="ADD",command=self.login,bg="orange",bd=5,fg="black",width=7,font="italic 15").place(x=180,y=340)
        self.root.mainloop()
        
        
        
    def login(self):
        username=self.entry1.get() # get use to fetch information
        password=self.entry2.get()
        if (username=="")and(password==""):
            messagebox.showerror('Error',"please enter your details")
        
        elif(username==""):
            messagebox.showerror('Error',"please enter your user name")
        elif(password==""):
            messagebox.showerror('Error',"please enter your pssword")
        else:
            self.data = (
                username,
                password,
            )
            res = userDatabase.login(self.data)
            if res:
                messagebox.showinfo('Success', 'Login Successfully.')
                self.openpage(res)
            else:
                messagebox.showerror('Alert', 'Invalid credentials')

    def openpage(self, res):
        self.root.destroy()
        obj = homeMenu.Labelwindow(res)
        obj.menus()
        
        
if __name__=="__main__":
    obj= Labelwindow()
    