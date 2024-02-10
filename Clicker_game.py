from tkinter import *
import time

count = 0
buyed = "no"
def click():
    global count
    if buyed == "yes":
        count += 2
    else:
        count += 1
    label.config(text = count)

def buy():
    global buyed
    if count >= 100:
        buyed = "yes"
        buy_two.pack_forget()
    else:
        label.config(text = "HAHAHA")

def button_configs():
    buy_two.config(command = buy)
    button.config(command = click)
    button.config(font = ("Ink Free", 50))
    button.config(bg = "#00FBFF")
    button.config(fg = "#F7FF00")
    button.config(activebackground = "#00FBFF")
    button.config(activeforeground = "#F7FF00")

window = Tk()
window.title("Clicker Showdown")
button = Button(window, text = "Click me!!")
buy_two = Button(window, text = "Click here to buy double clicks, clicks required: 100")
button_configs()
label = Label(window, text = count)
label.config(font = ("Monospace", 50))
label.pack()
buy_two.pack()
button.pack()
window.mainloop()
