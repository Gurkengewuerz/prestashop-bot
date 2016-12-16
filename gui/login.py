from tkinter import *
from tkinter import messagebox
from db import *
import time
import hashlib

db = DB()


class Application:
    def __init__(self):
        self.loginframe = Tk()
        self.loginframe.title("Administration Control Panel - Login")
        self.loginframe.resizable(width=FALSE, height=FALSE)
        self.loginframe.geometry("400x200")

        self.userImg = PhotoImage(file="./img/user.png")
        self.w1 = Label(self.loginframe, image=self.userImg).place(x=43, y=105)

        self.passImg = PhotoImage(file="./img/lock.png")
        self.w1 = Label(self.loginframe, image=self.passImg).place(x=205, y=106)

        self.passwordlb = Label(self.loginframe, text="Password")
        self.passwordlb.place(x=225, y=110)
        self.passVar = StringVar()
        self.passwordtb = Entry(self.loginframe, show="*", textvariable=self.passVar)
        self.passwordtb.place(x=210, y=130)

        self.usernamelb = Label(self.loginframe, text="Username")
        self.usernamelb.place(x=60,y=110)
        self.userVar = StringVar()
        self.usernametb = Entry(self.loginframe, textvariable=self.userVar)
        self.usernametb.place(x=45,y=130)

        self.loginbtn = Button(self.loginframe, text="Log In", command=self.checkContent)        #Login Button
        self.loginbtn.place(x=306,y=160)

        self.statlb = Label(self.loginframe, text="")
        self.statlb.place(x=45,y=160)

        self.loginframe.mainloop()

    def checkContent(self):
        print("Test")
        hashObj = hashlib.sha256(self.passVar.get().encode())
        userQuery = db.query("SELECT * FROM ita_user WHERE username = '%s' AND password = '%s'" % (self.userVar.get(), hashObj.hexdigest()))
        if len(userQuery.fetchall()):
            messagebox.showinfo("Information", "Login successful!", icon="info")
            time.sleep(1)
            quit(self)      #the mainframe is still running...
        else:
            messagebox.showinfo("Error", "Invalid username or password!", icon="error")

Application()

