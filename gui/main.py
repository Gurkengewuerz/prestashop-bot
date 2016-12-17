from tkinter import *
from tkinter import messagebox
from db import *
import time


db = DB()


class Mainframe:
    def __init__(self):
        self.main = Tk()
        self.main.iconbitmap(default="./img./user.ico")
        self.main.title("Administration Control Panel")
        self.main.resizable(width=FALSE, height=FALSE)
        self.main.geometry("340x380")

        self.main.mainloop()
Mainframe()