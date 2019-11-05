import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.n=0
        self.v=0
        self.filename=""
        self.title("Input Gui")
        self.labelFrame=ttk.LabelFrame(self,text = "Open an Image")
        self.labelFrame.grid(row=0,column=0)

        self.inputNumber()
        self.buttonSearch()
        self.radButton1()
        self.buttonSubmit()

    def inputNumber(self):
        self.inputNumber=ttk.Label(self.labelFrame,text="Number of matches")
        self.inputNumber.grid(row=3,column=0)
        n=Entry(self.labelFrame,width=10)
        n.grid(row=3,column=1)
        self.n=n.get()
        
    def buttonSearch(self):
        self.buttonSearch=ttk.Button(self.labelFrame,text= "Browse an Image",command=self.fileDialog)
        self.buttonSearch.grid(row=1,column=0,columnspan=2)        

    def fileDialog(self):
        self.filename= filedialog.askopenfilename(initialdir="Data\DataUji",title = "Select an Image",filetype=(("jpg","*.jpg"),("All File","*,*")))
        self.label=ttk.Label(self.labelFrame,text="")
        self.label.grid(row=2,column=0,columnspan=2)
        self.label.configure(text=self.filename)
        
   
    def radButton1(self):
        global v
        v=IntVar()
        v.set(1)
        self.label=ttk.Label(self.labelFrame,text="Choose your method:")
        self.label.grid(row=4,column=0)
        self.radButton2=ttk.Radiobutton(self.labelFrame,text="Euclidean Distance",variable=v,value=1,command= self.v<-v.get())
        self.radButton2.grid(row=5,column=0)
        self.radButton2=ttk.Radiobutton(self.labelFrame,text="Cosine distance",variable=v,value=2,command=self.v<-v.get())
        self.radButton2.grid(row=5,column=1)

    def show(self):
        x=str(self.n)+" "+str(self.v)+" "+self.filename
        self.label=ttk.Label(self.labelFrame,text=x)
        self.label.grid(row=7,column=0)
        print(self.n," ",self.v," ",self.filename)    
    
    def buttonSubmit(self):
        self.buttonSubmit=ttk.Button(self.labelFrame,text= "Send",command=self.show())
        self.buttonSubmit.grid(row=6,column=0)        


if __name__=='__main__':
    window = Window()
    window.mainloop()