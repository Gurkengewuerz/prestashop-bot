from tkinter import *
from tkinter import messagebox
from db import *
import time
import hashlib
from main import *


db = DB()


class Application:
    def __init__(self):
        self.loginframe = Tk()
        self.loginframe.iconbitmap(default="./img./user.ico")
        self.loginframe.title("Administration Control Panel")
        self.loginframe.resizable(width=FALSE, height=FALSE)
        self.loginframe.geometry("340x380")

        self.bgImg = PhotoImage(file="./img/bg_overlay.png")
        self.bg1 = Label(self.loginframe, image=self.bgImg).pack()

        self.passVar = StringVar()
        self.passwordtb = Entry(self.loginframe, show="*", textvariable=self.passVar)
        self.passwordtb.place(x=100, y=230)

        self.userVar = StringVar()
        self.usernametb = Entry(self.loginframe, textvariable=self.userVar)
        self.usernametb.place(x=100,y=160)

        self.loginbtn = Button(self.loginframe, command=self.checkContent, height = 1, width = 10,)        #Login Button
        self.loginbtn.place(x=130, y=280)
        #self.loginbtn.place(x=130,y=280)

        self.loginframe.mainloop()

    def checkContent(self):
        hashObj = hashlib.sha256(self.passVar.get().encode())
        userQuery = db.query("SELECT * FROM ita_user WHERE username = '%s' AND password = '%s'" % (self.userVar.get(), hashObj.hexdigest()))
        if len(userQuery.fetchall()):
            messagebox.showinfo("Information", "Login successful!", icon="info")
            time.sleep(1)
            quit(self)      #the mainframe is still running...
            create
        else:
            messagebox.showinfo("Error", "Invalid username or password!", icon="error")


Application()

