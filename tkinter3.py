from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text = "Hello World!")
    myLabel.pack()

myButton = Button(root, text = "Click Here", command = myClick, state = "active")
myButton.pack()

root.mainloop()