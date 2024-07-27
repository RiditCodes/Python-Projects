from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image")
root.iconbitmap("education_book.ico")

my_img = Image.open("book.jpg")
my_img = my_img.resize((900, 700), Image.LANCZOS)
my_img = ImageTk.PhotoImage(my_img)

my_label = Label(image = my_img)
my_label.pack()

root.mainloop()