from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image,ImageTk
import database

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

class Labelwindow:
  def __init__(self):  
    self.root=Toplevel()
    self.root.title(' QUIZ HUB ')
    self.root.resizable(FALSE,FALSE)
    self.root.geometry('900x600+400+100')

    self.frame1 = Frame(self.root)
    self.frame1.place(x = 0, y = 0, width=150, height=400)

    self.frame2 = Frame(self.root)
    self.frame2.place(x = 200, y = 0, width=750, height=400)

    res = database.allSubject()
    if res:
            self.options = res
    else:
        messagebox.showerror('Alert', 'Something went wrong.')

    self.subDrop = Combobox(self.frame1, values= self.options)
    self.subDrop.place(x = 4, y = 40)

    self.subDrop.insert(0, 'select subject')
    self.subDrop.bind("<<ComboboxSelected>>", self.getTopics)

    self.root.mainloop()


  def getTopics(self, e):
    a = list(self.subDrop.get().split())
    res = database.getTopics(a[0])
    print(res)
    if res:
        x = 4
        y = 80
        for i in res:
            self.topicLabel = Button(self.frame1, pady=5, text=i[2], command  =  lambda x = i[0]:  self.getTopicReport(x))
            self.topicLabel.place(x = x, y = y)

            y += 50
    else:
        messagebox.showerror('Alert', 'No Topics')


  def getTopicReport(self, x):
    for widget in self.frame2.winfo_children():
            widget.destroy()

    self.scoreList = database.getScores(x)
    if len(self.scoreList) == 0:
        messagebox.showerror('Alert', 'No data to show yet.')
    else:
        print(self.scoreList)
        a = []
        for i in self.scoreList:
            a.append(i[5])


        # the figure that will contain the plot
        fig = plt.Figure(figsize = (5, 5),
                        dpi = 100)

            # labels = ['Covered', 'Remaining']
            
            # data = [self.coveredHouses, self.expectedHouses]
            
            # Creating plot
        fig = plt.figure(figsize =(10, 7))
            # plt.pie(data, labels = labels, autopct='%1.2f%%')
        plt.plot(a, linestyle = 'dotted')
        
            # list of squares
            # y = [i**2 for i in range(101)]
        
            # adding the subplot
            # plot1 = fig.add_subplot(111)
        
            # plotting the graph
            # plot1.plot(y)
        
            # creating the Tkinter canvas
            # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig,
                                    master = self.frame2)  
        canvas.draw()
        
            # placing the canvas on the Tkinter window
        canvas.get_tk_widget().pack()
        
            # creating the Matplotlib toolbar
        toolbar = NavigationToolbar2Tk(canvas,
                                        self.frame2)
        toolbar.update()
        
            # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().pack()

if __name__ == "__main__":
    obj = Labelwindow()