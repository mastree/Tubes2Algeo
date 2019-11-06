from tkinter import *
from PIL import ImageTk, Image
window=Tk()
window.title('Face recognition interface')


img1= ImageTk.PhotoImage(Image.open("Data\DataUji\pins_Aaron PaulTest\Aaron Paul2_293.jpg"))
img2= ImageTk.PhotoImage(Image.open("Data\DataUji\pins_Amaury NolascoTest\Amaury Nolasco6.jpg"))
img3= ImageTk.PhotoImage(Image.open("Data\DataUji\pins_Alvaro MorteTest\Alvaro Morte16_879.jpg"))

imageList=[img1,img3,img2]
imageLabel=Label(image=img1)
imageLabel.grid(row=0,column=0,columnspan=3)

textLabel=Label(text="Nama")
textLabel.grid(row=1,column=0)
textLabel2=Label(text="Persentase Kemiripan")
textLabel2.grid(row=2,column=0,columnspan=2)


def next(imageNth):
    global imageLabel
    global buttonBack
    global buttonNext

    imageLabel.grid_forget()
    imageLabel = Label(image=imageList[imageNth-1])
    if(imageNth== len(imageList)):
        buttonNext=Button(window,text="-->",command=lambda:next(1))
        buttonBack=Button(window,text="<--",command=lambda:back(imageNth-1))
    else: 
        if(imageNth == 1):
            buttonNext=Button(window,text="-->",command=lambda:next(imageNth+1))
            buttonBack=Button(window,text="<--",command=lambda:back(len(imageList)))
        else:
            buttonNext=Button(window,text="-->",command=lambda:next(imageNth+1))
            buttonBack=Button(window,text="<--",command=lambda:back(imageNth-1))
    
    
    imageLabel.grid(row=0,column=0,columnspan=3)
    textLabel=Label(text="Nama")
    textLabel.grid(row=1,column=0)
    textLabel2=Label(text="Persentase Kemiripan")
    textLabel2.grid(row=2,column=0,columnspan=2)
    buttonBack.grid(row=3,column=0)
    buttonNext.grid(row=3,column=2)

def back(imageNth):
    global imageLabel
    global buttonBack
    global buttonNext

    imageLabel.grid_forget()
    imageLabel = Label(image=imageList[imageNth-1])

    if(imageNth== len(imageList)):
        buttonNext=Button(window,text="-->",command=lambda:next(1))
        buttonBack=Button(window,text="<--",command=lambda:back(imageNth-1))

    else:
        if (imageNth == 1):
            buttonNext=Button(window,text="-->",command=lambda:next(imageNth+1))
            buttonBack=Button(window,text="<--",command=lambda:back(len(imageList)))
        else:
            buttonNext=Button(window,text="-->",command=lambda:next(imageNth+1))
            buttonBack=Button(window,text="<--",command=lambda:back(imageNth-1))
    
    imageLabel.grid(row=0,column=0,columnspan=3)
    textLabel=Label(text="Nama")
    textLabel.grid(row=1,column=0)
    textLabel2=Label(text="Persentase Kemiripan")
    textLabel2.grid(row=2,column=0,columnspan=2)
    buttonBack.grid(row=3,column=0)
    buttonNext.grid(row=3,column=2)

buttonBack=Button(window,text= "<--",command=lambda: back(len(imageList)))
buttonExit=Button(window,text= "Exit",command=window.quit)
buttonNext=Button(window,text= "-->",command=lambda:next(2))
buttonBack.grid(row=3,column=0)
buttonExit.grid(row=3,column=1)
buttonNext.grid(row=3,column=2)
window.mainloop()