from tkinter import *

root = Tk()

e = Entry(root, width=50, fg="white", bg="blue")
e.pack()
e.insert(0,"Enter your name:")

def myClick():
	myLabel = Label(root,text="School")
	myLabel.pack()

myButton = Button(root, text="Click", command=myClick, padx=150, pady=50, 

fg="Blue", bg="green")
myButton.pack()

root.mainloop()
