from tkinter import *

root = Tk()


e = Entry(root, width=50, borderwidth=5)
e.pack()

def myClick():		
	variable1 = "Good evening " + e.get()
	myLabel = Label(root, text=variable1)
	myLabel.pack()


myButton = Button(root, text="Click me", command=myClick, padx=50, 

pady=50, fg="blue", bg="green")
myButton.pack()

root.mainloop()
