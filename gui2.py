import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
# import fecesrecognition as fr
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
        #self.showResult()
    def onClicked(self):
        s1=self.entry1.get()
        s2=self.method.get()
        if(s1.isdigit()):
            s1=int(s1)
            self.labelFrame.grid_forget()
            # self.photos,self.names,self.matches=fr.run(s1,s2,self.filename)
            
            # img1= ImageTk.PhotoImage(Image.open("Data\DataUji\pins_Aaron PaulTest\Aaron Paul2_293.jpg"))
            # img2= ImageTk.PhotoImage(Image.open("Data\DataUji\pins_Amaury NolascoTest\Amaury Nolasco6.jpg"))
            # img3= ImageTk.PhotoImage(Image.open("Data\DataUji\pins_Alvaro MorteTest\Alvaro Morte16_879.jpg"))

            # self.photos=[img1,img2,img3]
            # self.names=["a","b","c"]
            # self.matches=[90,80,70]

            self.showResult(1)
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
        
    def showResult(self,imageNth):
        
        self.label2=ttk.Label(self,image=self.photos[imageNth-1])
        self.label2.grid(row=0,column=0,columnspan=3)

        self.textLabel=ttk.Label(self,text="Nama : "+self.names[imageNth-1])
        self.textLabel.grid(row=1,column=0)
        self.textLabel2=ttk.Label(self,text="Persentase Kemiripan : "+str(self.matches[imageNth-1]))
        self.textLabel2.grid(row=2,column=0,columnspan=2)
        
        if(imageNth== len(self.photos)):
            self.buttonNext=ttk.Button(self,text="-->",command=lambda:self.showResult(1))
            self.buttonBack=ttk.Button(self,text="<--",command=lambda:self.showResult(imageNth-1))
        else: 
            if(imageNth == 1):
                self.buttonNext=ttk.Button(self,text="-->",command=lambda:self.showResult(imageNth+1))
                self.buttonBack=ttk.Button(self,text="<--",command=lambda:self.showResult(len(self.photos)))
            else:
                self.buttonNext=ttk.Button(self,text="-->",command=lambda:self.showResult(imageNth+1))
                self.buttonBack=ttk.Button(self,text="<--",command=lambda:self.showResult(imageNth-1))
        
        self.buttonExit=ttk.Button(self,text= "Exit",command=self.quit)
        self.buttonBack.grid(row=3,column=0)
        self.buttonExit.grid(row=3,column=1)
        self.buttonNext.grid(row=3,column=2)
     
if __name__=='__main__':
    window = Window()
    window.mainloop()