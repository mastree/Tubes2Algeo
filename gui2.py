import cv2
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
import fecesrecognition as fr
methods=[
    ("Euclidean Distance",1),
    ("Cosine distance",2)
]

class Window(Tk):
    def __init__(self):
        super(Window, self).__init__()

        self.title("Input Gui")
        
        
        self.labelFrame=ttk.LabelFrame(self,text = "Open an Image")
        self.labelFrame.grid(row=0,column=0,sticky=N+S+W+E)
        
        #browse picture
        self.buttonSearch()
        
        # radio button for method
        self.method=IntVar()
        self.method.set(1)
        self.radioLabel=ttk.Label(self.labelFrame,text="Choose your method : ")
        self.radioLabel.grid(row=3,columnspan=6)
        for val,choice in enumerate(methods):
            b=Radiobutton(self.labelFrame,text=choice[0],variable=self.method,value=choice[1])
            b.grid(row=4,column=val*3,columnspan=3)

        # spin box for how many matches
        self.spinText=ttk.Label(self.labelFrame, text = "Number of matches : ")
        self.spinText.grid(row = 5, column = 0, columnspan = 3)
        self.spinLabel=ttk.Spinbox(self.labelFrame, from_= 1, to = 20, width = 4)
        self.spinLabel.grid(row = 5, column = 3, columnspan = 3)

        #submit button
        self.buttonSubmit=ttk.Button(self.labelFrame,text="Send",command=self.onClicked)
        self.buttonSubmit.grid(row=6,column=0,columnspan=6)

    def buttonSearch(self):
        self.buttonSearch=ttk.Button(self.labelFrame,text= "Browse an Image",command=self.fileDialog)
        self.buttonSearch.grid(row=1,column=0,columnspan=6)

    def fileDialog(self):
        self.filename= filedialog.askopenfilename(initialdir="Data\DataUji",title = "Select an Image",filetype=(("jpg","*.jpg"),("All File","*,*")))
        self.label=ttk.Label(self.labelFrame,text="")
        self.label.grid(row=2,column=0,columnspan=6)
        self.label.configure(text=self.filename)
        

    def onClicked(self):
        s2=self.method.get()
        self.labelFrame.pack_forget()

        temp,self.matches,temp2=fr.find_match(self.filename, s2, int(self.spinLabel.get()))
        
        self.photos = [ImageTk.PhotoImage(Image.fromarray(foto,'RGB')) for foto in temp]
        self.tested = ImageTk.PhotoImage(Image.fromarray(temp2,'RGB'))
        self.showResult(1)
        
    def showResult(self,imageNth):
        
        self.label1=Label(self,image=self.tested,bg='black')
        self.label1.grid(row=0,column=0,sticky=N+S+W+E)

        self.label2=Label(self,image=self.photos[imageNth-1],bg='black')
        self.label2.grid(row=0,column=1,sticky=N+S+E+W)

        self.textLabel=Label(self,text="Ranking : "+str(imageNth)+" ("+str(self.matches[imageNth-1])+")",bg='black',fg='white')
        self.textLabel.grid(row=1,column=0,columnspan=2,sticky=N+S+W+E)
        
        if(imageNth== len(self.photos)):
            self.buttonNext=Button(self ,text="Next",bg='black',fg='white',command=lambda:self.showResult(1))
            self.buttonBack=Button(self ,text="Prev",bg='black',fg='white',command=lambda:self.showResult(imageNth-1))
        else: 
            if(imageNth == 1):
                self.buttonNext=Button(self ,text="Next",bg='black',fg='white',command=lambda:self.showResult(imageNth+1))
                self.buttonBack=Button(self ,text="Prev",bg='black',fg='white',command=lambda:self.showResult(len(self.photos)))
            else:
                self.buttonNext=Button(self ,text="Next",bg='black',fg='white',command=lambda:self.showResult(imageNth+1))
                self.buttonBack=Button(self ,text="Prev",bg='black',fg='white',command=lambda:self.showResult(imageNth-1))
        
        self.buttonExit=Button(self ,text= "Exit",bg='black',fg='white',command=self.quit)    
        self.buttonBack.grid(row=2,column=0,columnspan=2,sticky=N+S+W+E)
        self.buttonExit.grid(row=3,column=0,columnspan=2,sticky=N+S+W+E)
        self.buttonNext.grid(row=4,column=0,columnspan=2,sticky=N+S+W+E)
     
if __name__=='__main__':
    window = Window()
    Grid.rowconfigure(window,0,weight=1)
    Grid.columnconfigure(window,0,weight=1)
    window.mainloop()