from tkinter import *
from tkinter import messagebox
import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        print("Go")

        # configure the root window
        self.title('Tip Calculator')
        self.geometry('400x400')

        
        # label
        self.titlelabel = Label(self, text='Tip Calculator')
        self.titlelabel.pack()
        

        self.gridframe=Frame(self)
        self.gridframe.pack()

        print("Creating grid")
        self.bill_label=Label(self.gridframe,text="Bill")
        self.bill_label.grid(row=0,column=0)

        self.bill_entry=Entry(self.gridframe)
        self.bill_entry.grid(row=0,column=1)

        self.tip_label=Label(self.gridframe,text="Tip Percent")
        self.tip_label.grid(row=1,column=0)

        self.tippercent_entry=Entry(self.gridframe)
        self.tippercent_entry.grid(row=1,column=1)
        

        
        # button
        self.button = tk.Button(self, text='Calculate')
        self.button['command'] = self.calculate_tip
        self.button.pack()

        self.results_label=Label(self)
        self.results_label.pack()

        print("Done")

    def calculate_tip(self):
        #self.name=self.nameentry.get()
        #messagebox.showinfo(title='Information', message='Hello '+self.name+"!")
        self.bill=float(self.bill_entry.get())
        self.tippercent=int(self.tippercent_entry.get())
        self.tip=round(self.bill*(self.tippercent/100),2)
        self.totalbill=self.bill+self.tip

        self.results_label.config(text="Tip: "+str(self.tip)+" Total Bill: "+str(self.totalbill))

if __name__ == "__main__":
    app = App()
    app.mainloop()