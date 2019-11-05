import tkinter as tk
# import fecesrecognition as fr
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

methods=[
    ("Euclidean Distance",1),
    ("Cosine distance",2)
]
class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()
        self.n=0
        self.v=0
        self.filename=""
        self.title("Input Gui")
        self.labelFrame=ttk.LabelFrame(self,text = "Open an Image")
        self.labelFrame.grid(row=0,column=0)

        # inputing number of matches 
        self.entry1=Entry(self.labelFrame)
        self.entry1.insert(0,"Put number of expected matches here")
        self.entry1.grid(row=3,column=0)
        
        # radio button for method
        self.method=IntVar()
        self.method.set(1)
        for val,choice in enumerate(methods):
            b=Radiobutton(self.labelFrame,text=choice[0],variable=self.method,value=choice[1])
            b.grid(row=5,column=val)

        #submit button
        self.buttonSubmit=ttk.Button(self.labelFrame,text="Send",command=self.onClicked)
        self.buttonSubmit.grid(row=6,column=0)

        self.buttonSearch()

    def onClicked(self):
        s1=self.entry1.get()
        s2=self.method.get()
        if(s1.isdigit()):
            s1=int(s1)
            print(s1," ",s2," ",self.filename)
        else:
            messagebox.showerror("Error","Number must be an integer! please re-input")

    def buttonSearch(self):
        self.buttonSearch=ttk.Button(self.labelFrame,text= "Browse an Image",command=self.fileDialog)
        self.buttonSearch.grid(row=1,column=0)        

    def fileDialog(self):
        self.filename= filedialog.askopenfilename(initialdir="Data\DataUji",title = "Select an Image",filetype=(("jpg","*.jpg"),("All File","*,*")))
        self.label=ttk.Label(self.labelFrame,text="")
        self.label.grid(row=2,column=0,columnspan=2)
        self.label.configure(text=self.filename)
        


if __name__=='__main__':
    window = Window()
    window.mainloop()