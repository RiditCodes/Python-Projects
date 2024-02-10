from tkinter import messagebox, simpledialog, Tk
from random import choice
import string

def get_task():
    task = simpledialog.askstring("Task", "Do you want to encrypt or decrypt: ")
    return task

def get_message():
    message = simpledialog.askstring("Message", "Enter the message: ")
    return message

def is_even(number):
    return number % 2 == 0

def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters

def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message += "x"
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = "".join(letter_list)
    return new_message

def encrypt(message):
    encrypted_list = []
    fake_letters = list(string.ascii_lowercase)
    for counter in range(0, len(message)):
        encrypted_list.append(message[counter])
        encrypted_list.append(choice(fake_letters))
    new_message = "".join(encrypted_list)
    swapped_message = swap_letters(new_message)
    encrypted_message = "".join(reversed(swapped_message))
    return encrypted_message

def decrypt(message):
    unreversed_message = "".join(reversed(message))
    swapped_message = "".join(swap_letters(unreversed_message))
    even_letters = get_even_letters(swapped_message)
    decrypted_message = ''.join(even_letters)
    return decrypted_message

root = Tk()

while True:
    task = get_task()
    if task == "encrypt":
        message = get_message()
        encrypted = encrypt(message)
        messagebox.showinfo("Ciphertext of the secret message is: ", encrypted)
    elif task == "decrypt":
        message = get_message()
        encrypted = decrypt(message)
        messagebox.showinfo("Plaintext of the secret message is: ", encrypted)
    else:
        break
root.mainloop()
root.withdraw()