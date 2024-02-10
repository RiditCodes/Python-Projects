from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image")

my_img = Image.open("Msdos-icon.jpg")
my_img = my_img.resize((500, 500),Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(my_img)
my_label = Label(image=my_img)
my_label.pack()

root.mainloop()
