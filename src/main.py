import tkinter as tk
from summarizer import firstWord
import os

win = tk.Tk()
win.geometry("650x250")

# Title of the GUI 
label = tk.Label(win, text = "Article or Text Summarizer", font = ('Times New Roman bold',20))
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
textExample = tk.Text(win, relief = tk.RIDGE, height = 25, borderwidth = 2)
textExample.pack()


# Button Click 
btnRead = tk.Button(win, height = 2, width = 15, text = "Summarize", 
                    command = getTextInput)
btnRead.pack(pady = 15)

def refresh():
    btnRead.config(state = 'normal')
    refreshButton.config(state = 'disabled')
    textExample.delete('1.0', tk.END)
    textOutput.delete('1.0' , tk.END)


# Run it again
refreshButton = tk.Button(win, height = 2, width = 15, text="Try Again", command=refresh, state='disabled')
refreshButton.pack()

#Output Textbox
textOutput = tk.Text(win, relief = tk.RIDGE, height = 25, borderwidth = 2)
textOutput.pack()

#win.attributes('-fullscreen', True)
win.mainloop()