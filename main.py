import tkinter as tk

win = tk.Tk()
win.geometry("650x250")

label = tk.Label(win, text = "Article or Text Summarizer", font = ('Times New Roman bold',20))
label.pack(padx = 10, pady = 25)

def getTextInput():
    result = textExample.get(1.0, tk.END+"-1c")
    #result is the string to parse 

textExample = tk.Text(win, relief = tk.RIDGE, height = 25, borderwidth = 2)
textExample.pack()
btnRead = tk.Button(win, height = 1, width = 10, text = "Summarize", 
                    command = getTextInput)

btnRead.pack(pady = 15)

win.attributes('-fullscreen', True)
win.mainloop()