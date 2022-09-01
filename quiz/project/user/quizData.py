
import json
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import userDatabase, selectSubject
from tkinter import messagebox as mb


#class to define the components of the GUI
class Quiz:
    def __init__(self, root, question, option, answer, userRes, topicId, subId):

        self.gui = root
        self.answer = answer
        self.question = question
        self.options = option
        self.userRes = userRes
        self.topicId = topicId
        self.subId = subId
         
        # set question number to 0
        self.q_no=0
         
        # assigns ques to the display_question function to update later.
        self.display_title()
        self.display_question()
         
        # opt_selected holds an integer value which is used for
        # selected option in a question.
        self.opt_selected=IntVar()
         
        # displaying radio button for the current question and used to
        # display options for the current question
        self.opts=self.radio_buttons()
         
        # display options for the current question
        self.display_options()
         
        # displays the button for next and exit.
        self.buttons()
         
        # no of questions
        self.data_size=len(question)
         
        # keep a counter of correct answers
        self.correct=0
 
 
    # This method is used to display the result
    # It counts the number of correct and wrong answers
    # and then display them at the end as a message Box
    def display_result(self):
         
        # calculates the wrong count
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
         
        # calcultaes the percentage of correct answers
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        
        data = (
            self.userRes[0][0],
            self.subId, 
            self.topicId,
            self.correct,
            self.data_size
        )
        res = userDatabase.createScores(data)
        if res:
            # Shows a message box to display the result
            mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")
        else:
            mb.showerror('Alert', 'Something went wrong.')
        
 
 
    # This method checks the Answer after we click on Next.
    def check_ans(self, q_no):
        if (int(self.opt_selected.get()) - 1) == self.answer[q_no]:
            # if the option is correct it return true
            return True
 

    def next_btn(self):
         
        # Check if the answer is correct
        if self.check_ans(self.q_no):
             
            # if the answer is correct it increments the correct by 1
            self.correct += 1
         
        # Moves to next Question by incrementing the q_no counter
        self.q_no += 1
         
        # checks if the q_no size is equal to the data size
        if self.q_no==self.data_size:
             
            # if it is correct then it displays the score
            self.display_result()
             
            # destroys the self.gui
            self.gui.destroy()
            # obj = selectSubject.Labelwindow(self.userRes)
        else:
            # shows the next question
            self.display_question()
            self.display_options()
 
 

    def buttons(self):
         
        # The first button is the Next button to move to the
        # next Question
        next_button = Button(self.gui, text="Next",command=self.next_btn,
        width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
         
        # placing the button  on the screen
        next_button.place(x=350,y=380)
         
        # This is the second button which is used to Quit the self.gui
        quit_button = Button(self.gui, text="Quit", command=self.gui.destroy,
        width=5,bg="black", fg="white",font=("ariel",16," bold"))
         
        # placing the Quit button on the screen
        quit_button.place(x=700,y=50)
 
 
    def display_options(self):
        val=0
         
        # deselecting the options
        self.opt_selected.set(0)
         
        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in self.options[self.q_no]:
            self.opts[val]['text']=option
            val+=1
 
 
    # This method shows the current Question on the screen
    def display_question(self):
         
        # setting the Question properties
        q_no = Label(self.gui, text=self.question[self.q_no], width=60,
        font=( 'ariel' ,16, 'bold' ), anchor= 'w' )
         
        #placing the option on the screen
        q_no.place(x=70, y=100)
 
 
    # This method is used to Display Title
    def display_title(self):
         
        # The title to be shown
        title = Label(self.gui, text="QUIZ",
        width=50, bg="green",fg="white", font=("ariel", 20, "bold"))
         
        # place of the title
        title.place(x=0, y=2)
 
 
    # This method shows the radio buttons to select the Question
    # on the screen at the specified position. It also returns a
    # list of radio button which are later used to add the options to
    # them.
    def radio_buttons(self):
         
        # initialize the list with an empty list of options
        q_list = []
         
        # position of the first option
        y_pos = 150
         
        # adding the options to the list
        while len(q_list) < 4:
             
            # setting the radio button properties
            radio_btn = Radiobutton(self.gui,text=" ",variable=self.opt_selected,
            value = len(q_list)+1,font = ("ariel",14))
             
            # adding the button to the list
            q_list.append(radio_btn)
             
            # placing the button
            radio_btn.place(x = 100, y = y_pos)
             
            # incrementing the y-axis position by 40
            y_pos += 40
         
        # return the radio buttons
        return q_list

class quizData:
  def __init__(self, subId, topicId, userRes):
    self.topicId = topicId
    self.userRes = userRes

    self.root=Toplevel()
    self.root.title(' QUIZ HUB ')
    self.root.resizable(FALSE,FALSE)
    self.root.geometry('700x600+400+100')

    res = userDatabase.getQuestions(topicId)
    if res:
        # print(res)
        self.question, self.options, self.answer = self.getData(res)
        # print(self.question)
        print(self.options)
        # print(self.answer)

        quiz = Quiz(self.root, self.question, self.options, self.answer, self.userRes, topicId, subId)
    

    

    self.root.mainloop()

  def getData(self, res):
    ques = []
    option = []
    ans = []
    for i in res:
        # print(i[4])
        ques.append(i[2])
        ans.append(i[4])
        option.append(json.loads(i[3]))
    # print(ans)
    return (ques, option, ans)



if __name__=="__main__":
    obj= quizData()