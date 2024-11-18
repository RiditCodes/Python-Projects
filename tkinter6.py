from tkinter import *

root = Tk()

e = Entry(root, width = 50, fg = "black", bg = "red", borderwidth = 5)
e.pack()
e.insert(0, "Enter your name: ")

def myClick():
    var1 = "Hello " + e.get()
    myLabel = Label(root, text = var1)
    myLabel.pack()

myButton = Button(root, text = "Enter your name", command = myClick, padx = 50, pady = 50, fg = "blue", bg = "green")
myButton.pack()

root.mainloop()