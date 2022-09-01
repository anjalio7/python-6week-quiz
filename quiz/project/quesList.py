import json
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Treeview
import database
import editQues


class Labelwindow:
    def __init__(self):
        self.root = Toplevel()
        self.root.title(' QUIZ HUB ')
        self.root.resizable(FALSE, FALSE)
        self.root.geometry('700x600+400+100')

        self.fr = Frame(self.root, bg="white")
        self.fr.place(x=0, y=0, width="800", height="500")

        self.tr = Treeview(self.fr, columns=(
            'A', 'B', 'C', 'E', 'f', 'E', 'f', 'E', 'f', 'g'), selectmode="browse")

        self.tr.heading('#0', text="ID")
        self.tr.column('#0', minwidth=10, stretch=NO, width=100)

        self.tr.heading('#1', text="Topic")
        self.tr.column('#1', minwidth=1, stretch=NO, width=70)

        self.tr.heading('#2', text="Question")
        self.tr.column('#2', minwidth=2, stretch=NO, width=80)

        self.tr.heading('#3', text="Option1")
        self.tr.column('#3', minwidth=3,  stretch=NO, width=90)

        self.tr.heading('#4', text="Option2")
        self.tr.column('#4', minwidth=4, stretch=NO, width=100)

        self.tr.heading('#5', text="Option3")
        self.tr.column('#5', minwidth=4, stretch=NO, width=100)

        self.tr.heading('#6', text="Option4")
        self.tr.column('#6', minwidth=4, stretch=NO, width=100)

        self.tr.heading('#7', text="Answer")
        self.tr.column('#7', minwidth=4, stretch=NO, width=100)

        self.tr.heading('#8', text="Edit")
        self.tr.column('#8', minwidth=4, stretch=NO, width=100)

        self.tr.heading('#9', text="Delete")
        self.tr.column('#9', minwidth=4, stretch=NO, width=100)

        res = database.getQues()
        if res:
            a = []
            for i in res:
                b = []
                for j in range(len(i)):
                    if j != 3:
                        b.append(i[j])
                    else:
                        for k in json.loads(i[j]):
                            b.append(k)
                a.append(b)
            print(a)  
            for i in a:
                self.tr.insert('', 0, text = i[0], values = (i[1], i[2], i[3], i[4], i[5], i[6], i[7], 'Edit', 'Delete'))
        else:
            messagebox.showerror('Alert', 'Something went wrong.')

        self.tr.bind('<Double-Button-1>', self.actions)

        treeScroll = ttk.Scrollbar(self.root)
        treeScroll.configure(command=self.tr.xview)
        self.tr.configure(xscrollcommand=treeScroll.set)
        treeScroll.pack(side= RIGHT, fill= BOTH)

        self.tr.place(x=0, y=0, width="800", height="500")
        # # Add a Scrollbar(horizontal)
        # h=Scrollbar(self.root, orient='horizontal')
        # h.pack(side=BOTTOM, fill='x')
        self.root.mainloop()

    def actions(self, e):
        # get the values of the selected rows\\
        tt = self.tr.focus()
        col = self.tr.identify_column(e.x)
        print(f'col {col}')
        # print(self.tr.item(tt))

        gup = (
            self.tr.item(tt).get('text'),
        )
        if col == '#9':
            res = messagebox.askyesno(
                "Delete", "Do You Realy Want to delete this item.")
            if res:
                a = database.deleteQues(gup)
                if a:
                    messagebox.showinfo("Success", "Deleted Successfully")
                    self.root.destroy()
                    obj = Labelwindow()
                    # obj.Courses()
                else:
                    messagebox.showinfo("Alert", "Something went wrong")

        if col == '#8':
            self.root.destroy()
            obj = editQues.Labelwindow(gup)
            obj.comboWidget()


if __name__ == '__main__':
    obj = Labelwindow()
