from tkinter import *

root = Tk()
root.title("Icon")
root.iconbitmap("education_book.ico")

button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.pack()

root.mainloop()