import tkinter as tk
from summarizer import firstWord

win = tk.Tk()
win.geometry("650x250")

# Title of the GUI 
label = tk.Label(win, text = "Article or Text Summarizer", font = ('Times New Roman bold',20))
label.pack(padx = 10, pady = 25)

# Getting the inputs from the user 
def getTextInput():
    result = textExample.get(1.0, tk.END+"-1c")
    
    #firstWord(result)

# Textbox 
textExample = tk.Text(win, relief = tk.RIDGE, height = 25, borderwidth = 2)
textExample.pack()

# Button Click 
btnRead = tk.Button(win, height = 1, width = 10, text = "Summarize", 
                    command = getTextInput)
btnRead.pack(pady = 15)

#win.attributes('-fullscreen', True)
win.mainloop()