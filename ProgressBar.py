import tkinter.ttk as tkrtk
import tkinter as tkr

end_value = 100

def update_bar():
    global progress

    progress["value"] += 1
    progress.update()

def show_progress(max_val):
    global end_value
    global progress
    global windowkon

    windowkon = tkr.Tk()
    windowkon.title("Processing..")
    windowkon.geometry("400x30")
    end_value = max_val
    progress = tkrtk.Progressbar(windowkon, orient = "horizontal", length=400, mode = "determinate")
    progress.pack(side = "top")
    progress["value"] = 0
    progress["maximum"] = end_value

def close_bar():
    global progress
    global windowkon
    
    windowkon.destroy()