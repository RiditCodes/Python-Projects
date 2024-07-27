from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image")
root.iconbitmap("education_book.ico")

my_img = ImageTk.PhotoImage(Image.open("book.jpg"))
my_label = Label(image = my_img)
my_label.pack()

root.mainloop()