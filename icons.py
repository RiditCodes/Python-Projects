from tkinter import *

root = Tk()
root.title("Icon")
root.iconbitmap(r"C:\Users\Ridit\OneDrive\Python Projects\spaceship.ico")

button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.pack()
root.mainloop()
