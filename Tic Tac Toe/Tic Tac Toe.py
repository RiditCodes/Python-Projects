from importlib.machinery import WindowsRegistryFinder
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")
#root.iconbitmap("index.ico")

clicked = True
count = 0

def Button_click(btn):
    global clicked, count

    if btn["text"] == " " and clicked == True:
        btn["text"]  = "X"
        clicked = False
        count += 1
        CheckIfWon()

    elif btn["text"] == " " and clicked == False:
        btn["text"]  = "O"
        clicked = True
        count += 1
        CheckIfWon()
    else:
        messagebox.showerror("Tic Tac Toe", "The box has already been selected. \nPick another box.")

def disable_all_buttons():
    Button_1.config(state=DISABLED)
    Button_2.config(state=DISABLED)
    Button_3.config(state=DISABLED)
    Button_4.config(state=DISABLED)
    Button_5.config(state=DISABLED)
    Button_6.config(state=DISABLED)
    Button_7.config(state=DISABLED)
    Button_8.config(state=DISABLED)
    Button_9.config(state=DISABLED)

def CheckIfWon():
    global winner
    winner = False

#X win
    if Button_1["text"] == "X" and Button_2["text"] == "X" and Button_3["text"] == "X":
        Button_1.config(bg = "red")
        Button_2.config(bg = "red")
        Button_3.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins!")
        disable_all_buttons()

    elif Button_4["text"] == "X" and Button_5["text"]== "X" and Button_6["text"] == "X":
        Button_4.config(bg = "red")
        Button_5.config(bg = "red")
        Button_6.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins!")
        disable_all_buttons()
    
    elif Button_7["text"] == "X" and Button_8["text"]== "X" and Button_9["text"] == "X":
        Button_7.config(bg = "red")
        Button_8.config(bg = "red")
        Button_9.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins!")
        disable_all_buttons()

    elif Button_1["text"] == "X" and Button_4["text"]== "X" and Button_7["text"] == "X":
        Button_1.config(bg = "red")
        Button_4.config(bg = "red")
        Button_7.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins!")
        disable_all_buttons()

    elif Button_2["text"] == "X" and Button_5["text"]== "X" and Button_8["text"] == "X":
        Button_2.config(bg = "red")
        Button_5.config(bg = "red")
        Button_8.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins!")
        disable_all_buttons()

    elif Button_3["text"] == "X" and Button_6["text"]== "X" and Button_9["text"] == "X":
        Button_3.config(bg = "red")
        Button_6.config(bg = "red")
        Button_9.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins!")
        disable_all_buttons()

    elif Button_1["text"] == "X" and Button_5["text"]== "X" and Button_9["text"] == "X":
        Button_1.config(bg = "red")
        Button_5.config(bg = "red")
        Button_9.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins!")
        disable_all_buttons()

    elif Button_3["text"] == "X" and Button_5["text"]== "X" and Button_7["text"] == "X":
        Button_3.config(bg = "red")
        Button_5.config(bg = "red")
        Button_7.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins!")
        disable_all_buttons()

#O win
    if Button_1["text"] == "O" and Button_2["text"]== "O" and Button_3["text"] == "O":
        Button_1.config(bg = "red")
        Button_2.config(bg = "red")
        Button_3.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins!")
        disable_all_buttons()

    elif Button_4["text"] == "O" and Button_5["text"]== "O" and Button_6["text"] == "O":
        Button_4.config(bg = "red")
        Button_5.config(bg = "red")
        Button_6.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins!")
        disable_all_buttons()

    elif Button_7["text"] == "O" and Button_8["text"]== "O" and Button_9["text"] == "O":
        Button_7.config(bg = "red")
        Button_8.config(bg = "red")
        Button_9.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins!")
        disable_all_buttons()

    elif Button_1["text"] == "O" and Button_4["text"]== "O" and Button_7["text"] == "O":
        Button_1.config(bg = "red")
        Button_4.config(bg = "red")
        Button_7.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins!")
        disable_all_buttons()

    elif Button_2["text"] == "O" and Button_5["text"]== "O" and Button_8["text"] == "O":
        Button_2.config(bg = "red")
        Button_5.config(bg = "red")
        Button_8.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins!")
        disable_all_buttons()

    elif Button_3["text"] == "O" and Button_6["text"]== "O" and Button_9["text"] == "O":
        Button_3.config(bg = "red")
        Button_6.config(bg = "red")
        Button_9.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins!")
        disable_all_buttons()

    elif Button_1["text"] == "O" and Button_5["text"]== "O" and Button_9["text"] == "O":
        Button_1.config(bg = "red")
        Button_5.config(bg = "red")
        Button_9.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins!")
        disable_all_buttons()

    elif Button_3["text"] == "O" and Button_5["text"]== "O" and Button_7["text"] == "O":
        Button_3.config(bg = "red")
        Button_5.config(bg = "red")
        Button_7.config(bg = "red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins!")
        disable_all_buttons()

def reset():
    global Button_1, Button_2, Button_3, Button_4, Button_5, Button_6, Button_7, Button_8, Button_9
    global clicked, count
    clicked = True
    count = 0

    Button_1 = Button(root, text = " ", font = ("Helvetica", 20), height = 3, width = 6, bg = "cyan", command=lambda: Button_click(Button_1))
    Button_2 = Button(root, text = " ", font = ("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command=lambda: Button_click(Button_2))
    Button_3 = Button(root, text = " ", font = ("Helvetica", 20), height = 3, width = 6, bg = "cyan", command=lambda: Button_click(Button_3))
    Button_4 = Button(root, text = " ", font = ("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command=lambda: Button_click(Button_4))
    Button_5 = Button(root, text = " ", font = ("Helvetica", 20), height = 3, width = 6, bg = "cyan", command=lambda: Button_click(Button_5))
    Button_6 = Button(root, text = " ", font = ("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command=lambda: Button_click(Button_6))
    Button_7 = Button(root, text = " ", font = ("Helvetica", 20), height = 3, width = 6, bg = "cyan", command=lambda: Button_click(Button_7))
    Button_8 = Button(root, text = " ", font = ("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command=lambda: Button_click(Button_8))
    Button_9 = Button(root, text = " ", font = ("Helvetica", 20), height = 3, width = 6, bg = "cyan", command=lambda: Button_click(Button_9))

    Button_1.grid(row = 0, column = 0)
    Button_2.grid(row = 0, column = 1)
    Button_3.grid(row = 0, column = 2)
    Button_4.grid(row = 1, column = 0)
    Button_5.grid(row = 1, column = 1)
    Button_6.grid(row = 1, column = 2)
    Button_7.grid(row = 2, column = 0)
    Button_8.grid(row = 2, column = 1)
    Button_9.grid(row = 2, column = 2)

my_menu = Menu(root)
root.config(menu = my_menu)

options_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label = "Options", menu = options_menu)
options_menu.add_command(label = "Reset Game", command = reset)

root.mainloop()