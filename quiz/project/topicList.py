from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
import database
import editTopic


class Labelwindow:
    def __init__(self):
        self.root = Toplevel()
        self.root.title(' QUIZ HUB ')
        self.root.resizable(FALSE, FALSE)
        self.root.geometry('700x600+400+100')

        self.fr = Frame(self.root, bg="white")
        self.fr.place(x=0, y=0, width="800", height="500")

        self.tr = Treeview(self.fr, columns=(
            'A', 'B', 'C', 'E', 'f'), selectmode="extended")

        self.tr.heading('#0', text="ID")
        self.tr.column('#0', minwidth=10, stretch=NO, width=100)

        self.tr.heading('#1', text="subject")
        self.tr.column('#1', minwidth=1, stretch=NO, width=70)

        self.tr.heading('#2', text="Topic")
        self.tr.column('#2', minwidth=2, stretch=NO, width=80)

        self.tr.heading('#3', text="Edit")
        self.tr.column('#3', minwidth=3,  stretch=NO, width=90)

        self.tr.heading('#4', text="Delete")
        self.tr.column('#4', minwidth=4, stretch=NO, width=100)

        res = database.allTopics()
        if res:
            for i in res:
                self.tr.insert('', 0, text=i[0], values=(
                    i[1], i[2], 'Edit', 'Delete'))
        else:
            messagebox.showerror('Alert', 'Something went wrong.')

        self.tr.bind('<Double-Button-1>', self.actions)

        self.tr.place(x=0, y=0, width="800", height="500")

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
        if col == '#4':
            res = messagebox.askyesno(
                "Delete", "Do You Realy Want to delete this item.")
            if res:
                a = database.deleteTopic(gup)
                if a:
                    messagebox.showinfo("Success", "Deleted Successfully")
                    self.root.destroy()
                    obj = Labelwindow()
                    # obj.Courses()
                else:
                    messagebox.showinfo("Alert", "Something went wrong")

        if col == '#3':
            self.root.destroy()
            obj = editTopic.editTopic(gup)
            obj.comboWidget()


if __name__ == '__main__':
    obj = Labelwindow()
