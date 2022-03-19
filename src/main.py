import tkinter as tk
from summarizer import firstWord
import os

win = tk.Tk()
win.geometry("650x250")

frame= tk.Frame(win, relief= 'sunken', bg= "white")
frame.pack(fill= tk.BOTH, expand= True, padx= 10, pady=50)

# Title of the GUI 
label = tk.Label(frame, text = "Article or Text Summarizer", font = ('Times New Roman bold',20))
label.pack(padx = 10, pady = 25)


# Getting the inputs from the user 
def getTextInput():
    global out

    result = textExample.get(1.0, tk.END+"-1c")
    returnLetter = firstWord(result)
    textOutput.insert("1.0" , returnLetter)

    btnRead['text'] = "Text Summarized"
    btnRead.config(state = 'disabled')
    refreshButton.config(state = 'normal')
    btnRead.update()

    return
    
# Textbox 
textExample = tk.Text(frame, relief = tk.RIDGE, height = 25, borderwidth = 2)
textExample.pack(side = tk.LEFT)


# Button Click 
btnRead = tk.Button(frame, height = 2, width = 15, text = "Summarize", 
                    command = getTextInput)
btnRead.pack(pady = 15)#, side = tk.BOTTOM)
btnRead.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

def refresh():
    btnRead.config(state = 'normal')
    refreshButton.config(state = 'disabled')
    textExample.delete('1.0', tk.END)
    textOutput.delete('1.0' , tk.END)


# Run it again
refreshButton = tk.Button(frame, height = 2, width = 15, text="Try Again", command=refresh, state='disabled')
refreshButton.pack(side = tk.TOP)
refreshButton.place(relx = 0.5, rely = 0.5, anchor=tk.CENTER)

#Output Textbox
textOutput = tk.Text(frame, relief = tk.RIDGE, height = 25, borderwidth = 2)
textOutput.pack(pady = 15, side = tk.RIGHT)

win.attributes('-fullscreen', True)
win.mainloop()