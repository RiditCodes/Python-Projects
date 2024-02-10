from tkinter import *
import webbrowser

root = Tk()
root.title("Shortcuts")

def py2exe_open():
    webbrowser.open_new_tab("https://stackabuse.com/creating-executable-files-from-python-scripts-with-py2exe/")

py2exe = Button(root, text="Create Executable Files from Python Scripts with py2exe", command=py2exe_open)
py2exe.pack()

def youtube_open():
    webbrowser.open_new_tab("https://www.youtube.com")

youtube = Button(root, text="Open youtube.com", command=youtube_open)
youtube.pack()

def coding_class_open():
    webbrowser.open_new_tab("https://meet.google.com/eip-frts-tip")

coding_class = Button(root, text="Run Coding Class", command=coding_class_open)
coding_class.pack()
