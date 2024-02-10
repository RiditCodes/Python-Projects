import tkinter
from tkinter import messagebox

def click():
    t1 = first_name.get(1.0, "end-1c")
    t2 = last_name.get(1.0, "end-1c")
    messagebox.showinfo(message=f"Your full name is: {t1} {t2}")

def textbox_switch():
    if tk.focus_get() == first_name:
        last_name.focus()
    elif tk.focus_get() == last_name:
        first_name.focus()

tk = tkinter.Tk(className="Full name")
tk.geometry("350x150")

first_name = tkinter.Text(height = 1, width = 10, fg="green")
last_name = tkinter.Text(height = 1, width = 10, fg="green")

first_lbl = tkinter.Label(text = "Enter first name: ")
last_lbl = tkinter.Label(text = "Enter last name: ")

pr = tkinter.Button(text="Show full name", command = click)

first_lbl.grid(column=0, row=0)
first_name.grid(column=1, row=0)
last_lbl.grid(column=0, row=1)
last_name.grid(column=1, row=1)

pr.grid(column=1, row = 2)

first_name.focus()
tk.bind("<Tab>", textbox_switch)

tk.mainloop()