from tkinter import *
from tkinter import filedialog

from japp import Japp

def open_file(master: Japp) -> None:
    filename = filedialog.askopenfile(mode="r")

    with open(filename, "r"):
        content = filename.read()

    master.text.textarea.delete(INSERT, END)
    master.text.textarea.insert(INSERT, content)
