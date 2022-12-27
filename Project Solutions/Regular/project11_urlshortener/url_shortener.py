from tkinter import *
from tkinter import messagebox
import tkinter as tk

class App(tk.Tk):
    def readinfo(self):

        pass

    def __init__(self):
        super().__init__()

        self.neworig=""
        self.newshort=""

        self.oldorig=""
        self.oldshort=""

        # configure the root window
        self.title('My Awesome App')
        self.geometry('500x300')

        self.titlelabel=tk.Label(self,text="URL Shortener")
        self.titlelabel.config(font="Arial 25")
        self.titlelabel.pack()

        self.resultslabel=tk.Label(self)
        self.resultslabel.pack()

        self.tableframe=tk.Frame(self)
        self.tableframe.pack()

        # label
        self.label = tk.Label(self.tableframe, text='Original URL: ')
        self.label.grid(column=0,row=0)

        self.entry=tk.Entry(self.tableframe)
        self.entry.grid(column=1,row=0)

        self.label2 = tk.Label(self.tableframe, text='New URL: ')
        self.label2.grid(column=0,row=1)

        self.entry2=tk.Entry(self.tableframe)
        self.entry2.grid(column=1,row=1)

        # button
        self.button = tk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack()

    def button_clicked(self):
        self.neworig==self.entry.get()
        self.newshort=self.entry2.get()
        
        myfile=open("result.txt","a")
        if(self.neworig!=self.oldorig or self.newshort!=self.oldshort):
            res=""
            res+=self.neworig
            res+="\n"
            res+=self.newshort
            res+="\n"
            myfile.write(res)

            self.oldorig=self.neworig
            self.oldshort=self.newshort
            
            self.resultslabel.config(text="Data Saved")


if __name__ == "__main__":
    app = App()
    app.mainloop()