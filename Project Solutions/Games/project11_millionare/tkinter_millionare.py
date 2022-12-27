from tkinter import *
import tkinter as tk
from functools import partial, update_wrapper
from threading import Event
import time

class Question:
    def __init__(self,question,options,answer):
        self.question=question
        self.options=options
        self.answer=answer
        self.writtenanswer=self.options[self.answer]

    def __str__(self):
        res=""
        res+="question\n"
        for i in range(len(self.options)):
            res+=self.options[i]+"\n"
        res+=str(self.answer)
        return res

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.setupquestions()

        self.pixel = tk.PhotoImage(width=1, height=1)
        image = self.pixel,
        # configure the root window
        self.title('Tkinter Millionare')
        self.geometry('500x500')
        self.delaytime=1500

        self.startframe=Frame(self)
        self.startlabel=Label(self.startframe,text="Who wants to be a Python Millionare",font="Calibri 32")
        self.startlabel.pack()
        self.startbutton=Button(self.startframe,compound="center",image=self.pixel,text="Start",command=self.startgame)
        self.startbutton.pack()
        self.startframe.pack()

        self.questionframe=Frame(self)

        self.questiononlabel=Label(self.questionframe, text='Question 1',font="Calibri 32")
        self.questiononlabel.pack()

        # label
        self.questionlabel = Label(self.questionframe, text='Question')
        self.questionlabel.pack()

        self.optionbuttons=[]
        for i in range(4):
            buttonfunction = partial(self.submitanswer,i)
            self.optionbutton=Button(self.questionframe,compound="center",image=self.pixel,text="Option "+str(i+1),command=buttonfunction)
            self.optionbutton.config(width=200,height=60)
            self.optionbutton.pack(pady=10)
            self.optionbuttons.append(self.optionbutton)

        self.answerframe=Frame(self)
        self.answerlabel=Label(self.answerframe,text="The answer is\nAnswer")
        self.answerlabel.config(font="Calibri 32")
        self.answerlabel.pack()
        self.resultlabel=Label(self.answerframe,text="Correct")
        self.resultlabel.configure(font="Calibri 32")
        self.resultlabel.pack()

        #self.displayquestion()

    def setupquestions(self):
        self.questions=[]
        myfile=open("questions.txt","r")
        lines=myfile.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i]. rstrip('\n') 
            lines[i] = lines[i]. strip('\ufeff') 
        
        self.questionon=0
        for i in range(0,len(lines),7):
            question=lines[i]
            option0=lines[i+1]
            option1=lines[i+2]
            option2=lines[i+3]
            option3=lines[i+4]
            answer=int(lines[i+5])
            self.questions.append(Question(question,[option0,option1,option2,option3],answer))
        print(self.questions[0])
    
    def displayquestion(self):
        self.questionframe.pack()
        self.answerframe.pack_forget()
        curquestion=self.questions[self.questionon]
        self.questiononlabel.config(text="Question "+str(self.questionon+1))
        self.questionlabel.config(text=curquestion.question)
        for i in range(4):
            self.optionbuttons[i].config(text=curquestion.options[i])

    def displaywinner(self):
        self.resultlabel.config(text="You win!")
        self.resultlabel.after(self.delaytime*2,self.mainmenu)

    def handleanswer(self,num):
        curquestion=self.questions[self.questionon]
        self.answerlabel.config(text=curquestion.writtenanswer)
        if(curquestion.answer==num):
            self.resultlabel.config(text="Correct")
            self.questionon+=1
            if(self.questionon<len(self.questions)):
                self.answerframe.after(self.delaytime,self.displayquestion)
            else:
                self.answerframe.after(self.delaytime,self.displaywinner)
        else:
            print("Incorrect")
            self.resultlabel.config(text="Incorrect")
            self.questionon=0
            self.answerframe.after(self.delaytime,self.mainmenu)


    def submitanswer(self,num):
        self.questionframe.pack_forget()
        self.answerframe.pack()

        self.answerlabel.config(text="The answer is...")
        self.resultlabel.config(text="")
        print("Submit answer",num)

        handleanswerfunction = partial(self.handleanswer,num)
        handleanswerfunction.__name__=""
        self.answerframe.after(self.delaytime,handleanswerfunction)
    
    def startgame(self):
        self.startframe.pack_forget()
        self.displayquestion()
        self.questionframe.pack()

    def mainmenu(self):
        self.answerframe.pack_forget()
        self.questionframe.pack_forget()
        self.startframe.pack()
        

if __name__ == "__main__":
    app = App()
    app.mainloop()