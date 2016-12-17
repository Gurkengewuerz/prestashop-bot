from tkinter import *
from tkinter import messagebox
from db import *
import time
import hashlib
import webbrowser


db = DB()


class Application:
    def __init__(self):
        self.loginframe = Tk()
        self.loginframe.iconbitmap(default="./img./ico.ico")
        self.loginframe.title("Administration Control Panel")
        self.loginframe.resizable(width=FALSE, height=FALSE)
        self.loginframe.geometry("340x460")

        self.bgImg = PhotoImage(file="./img/bg_overlay.png")
        self.bg1 = Label(self.loginframe, image=self.bgImg).pack()

        self.passVar = StringVar()
        self.passwordtb = Entry(self.loginframe, show="*", textvariable=self.passVar)
        self.passwordtb.place(x=100, y=285)

        self.ubImg = PhotoImage(file="./img/field.png")
        self.userVar = StringVar()
        self.usernametb = Entry(self.loginframe, textvariable=self.userVar)
        self.usernametb.place(x=100,y=238)

        self.btnImg = PhotoImage(file="./img/button.png")
        self.loginbtn = Button(self.loginframe, command=self.checkContent, height=33, width=149, image=self.btnImg)        #Login Button
        self.loginbtn.place(x=99, y=330)

        #self.visitLbl = Label(self.loginframe, text="PrestaShop-Bot", fg="blue", bg= null)
        #self.visitLbl.place(x=140, y=430)
        #self.visitLbl.bind("<Button-1>", callback)
        self.loginframe.mainloop()

    def checkContent(self):
        hashObj = hashlib.sha256(self.passVar.get().encode())
        userQuery = db.query("SELECT * FROM ita_user WHERE username = '%s' AND password = '%s'" % (self.userVar.get(), hashObj.hexdigest()))
        if len(userQuery.fetchall()):
            messagebox.showinfo("Information", "Login successful!", icon="info")
            time.sleep(1)
            quit(self)      #the mainframe is still running...
        else:
            messagebox.showinfo("Error", "Invalid username or password!", icon="error")

    #def callback(event):
        #webbrowser.open_new(r"http://www.google.com")

Application()
