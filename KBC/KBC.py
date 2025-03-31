from tkinter import *
from PIL import Image, ImageTk
from pygame import mixer

current_question = 1

def correct(event):
    correct_sound.play()
    event.widget.config(bg="green", fg="white")
    root.after(5000, next_question)

def incorrect(event, correct_button):
    event.widget.config(bg="red", fg="white")
    correct_button.config(bg="green", fg="white")
    wrong_sound.play()
    root.after(5000, next_question)

def next_question():
    global current_question
    if current_question == 1:
        current_question += 1
        question2()
    elif current_question == 2:
        current_question += 1
        question3()
    elif current_question == 3:
        root.destroy()
        print("The End")

def start():
    play.destroy()
    logo_label.destroy()
    question1()
    
def question1():
    question_sound.play()
    question = Label(root, text="Who is the prime minister of India?", font=("Arial", 20), bg="purple", fg="white")
    question.place(x = 300, y = 5)

    option1 = Button(root, text="Narendra Modi", font=("Arial", 20), bg="purple", fg="white", width=20, height=2)
    option1.place(x = 100, y = 150)

    option2 = Button(root, text="Rahul Gandhi", font=("Arial", 20), bg="purple", fg="white", width=20, height=2)
    option2.place(x = 500, y = 150)

    option3 = Button(root, text="Amit Shah", font=("Arial", 20), bg="purple", fg="white", width=20, height=2)
    option3.place(x = 100, y = 300)

    option4 = Button(root, text="Yogi Adityanath", font=("Arial", 20), bg="purple", fg="white", width=20, height=2)
    option4.place(x = 500, y = 300)

    option1.bind("<Button-1>", correct)
    option2.bind("<Button-1>", lambda event: incorrect(event, option1))
    option3.bind("<Button-1>", lambda event: incorrect(event, option1))
    option4.bind("<Button-1>", lambda event: incorrect(event, option1))

def question2():
    question_sound.play()

    for widget in root.winfo_children():
        widget.destroy()

    background_label = Label(root, image=bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    question = Label(root, text="During the recent Delhi elections, which party won the most seats in the legislature", font=("Arial", 20), bg="purple", fg="white")
    question.place(x = 0, y = 5)

    option1 = Button(root, text="Aam Aadmi Party", font=("Arial", 20), bg="purple", fg="white", width=20, height=2)
    option1.place(x = 100, y = 150)

    option2 = Button(root, text="Bhartiya Janta Party", font=("Arial", 20), bg="purple", fg="white", width=20, height=2)
    option2.place(x = 500, y = 150)

    option3 = Button(root, text="Congress", font=("Arial", 20), bg="purple", fg="white", width=20, height=2)
    option3.place(x = 100, y = 300)

    option4 = Button(root, text="Communist Party of India", font=("Arial", 20), bg="purple", fg="white", width=20, height=2)
    option4.place(x = 500, y = 300)

    option1.bind("<Button-1>", lambda event: incorrect(event, option2))
    option2.bind("<Button-1>", correct)
    option3.bind("<Button-1>", lambda event: incorrect(event, option2))
    option4.bind("<Button-1>", lambda event: incorrect(event, option2))

def question3():
    question_sound.play()

    for widget in root.winfo_children():
        widget.destroy()

    background_label = Label(root, image=bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    question = Label(root, text="What is the capital of France?", font=("Arial", 20), bg="purple", fg="white")
    question.place(x = 300, y = 5)

    option1 = Button(root, text="Madrid", font=("Arial", 20), bg="purple", fg="white", width=20, height=2)
    option1.place(x = 100, y = 150)

    option2 = Button(root, text="London", font=("Arial", 20), bg="purple", fg="white", width=20, height=2)
    option2.place(x = 500, y = 150)

    option3 = Button(root, text="Berlin", font=("Arial", 20), bg="purple", fg="white", width=20, height=2)
    option3.place(x = 100, y = 300)

    option4 = Button(root, text="Paris", font=("Arial", 20), bg="purple", fg="white", width=20, height=2)
    option4.place(x = 500, y = 300)

    option1.bind("<Button-1>", lambda event: incorrect(event, option4))
    option2.bind("<Button-1>", lambda event: incorrect(event, option4))
    option3.bind("<Button-1>", lambda event: incorrect(event, option4))
    option4.bind("<Button-1>", correct)

root = Tk()
root.title("Kaun Banega Crorepati")
root.iconbitmap(r"c:\Users\Ridit\OneDrive\Documents\Python_Projects\KBC\assets\KBC.ico")
root.geometry("1000x560")

mixer.init()
question_sound = mixer.Sound(r"C:\Users\Ridit\OneDrive\Documents\Python_Projects\KBC\assets\kbc-question.mp3")
wrong_sound = mixer.Sound(r"C:\Users\Ridit\OneDrive\Documents\Python_Projects\KBC\assets\wrong.mp3")
intro = mixer.Sound(r"C:\Users\Ridit\OneDrive\Documents\Python_Projects\KBC\assets\intro.mp3")
correct_sound = mixer.Sound(r"C:\Users\Ridit\OneDrive\Documents\Python_Projects\KBC\assets\correct-answer.mp3")
intro.play()

image = Image.open(r"C:\Users\Ridit\OneDrive\Documents\Python_Projects\KBC\assets\bg.png")
bg = ImageTk.PhotoImage(image)
background_label = Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

logo = PhotoImage(file=r"C:\Users\Ridit\OneDrive\Documents\Python_Projects\KBC\assets\logo.png")
logo_label = Label(root, image=logo)
logo_label.pack()

play = Button(root, text="Play", font=("Arial", 20), bg="green", fg="white", width=10, height=2, command=start)
play.pack()

root.mainloop()