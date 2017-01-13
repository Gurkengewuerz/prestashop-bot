from tkinter import *
from tkinter import messagebox
from db import *
import time
import hashlib
import webbrowser
from main import *

class Application():
    def __init__(self):
        self.db = DB()
        self.db.connect()

        self.loginframe = Tk()
        self.loginframe.iconbitmap(default="./img./ico.ico")
        self.loginframe.title("Administration Control Panel")
        self.loginframe.resizable(width=FALSE, height=FALSE)
        self.loginframe.geometry("340x460")

        self.bgImg = PhotoImage(file="./img/bg_overlay_status.png")
        self.bg1 = Label(self.loginframe, image=self.bgImg).pack()

        self.passVar = StringVar()
        self.passwordTb = Entry(self.loginframe, show="*", textvariable=self.passVar)
        self.passwordTb.place(x=100, y=285)

        self.ubImg = PhotoImage(file="./img/field.png")
        self.userVar = StringVar()
        self.usernameTb = Entry(self.loginframe, textvariable=self.userVar)
        self.usernameTb.place(x=100, y=238)

        self.btnImg = PhotoImage(file="./img/button.png")
        self.loginBtn = Button(self.loginframe, command=self.checkContent, height=33, width=149,
                               image=self.btnImg)  # Login Button
        self.loginBtn.place(x=99, y=330)

        self.visitLbl = Label(self.loginframe, text="PrestaShop-Bot", fg="blue")
        self.visitLbl.place(x=140, y=430)
        self.visitLbl.bind("<Button-1>", self.visitUs)

        statusvar = StringVar()
        statusvar.set("MySQL Online")
        self.statusLbl = Label(self.loginframe, text="Online", bg="white", fg="green")
        self.statusLbl.place(x=160, y=200)
        # MySQL QUERY = "SELECT VERSION()"

        self.loginframe.mainloop()  # MAINLOOP END

    def checkContent(self):
        hashObj = hashlib.sha256(self.passVar.get().encode())
        userQuery = self.db.query("SELECT * FROM ita_user WHERE username = '%s' AND password = '%s'" % (self.userVar.get(), hashObj.hexdigest()))
        if len(userQuery.fetchall()):
            Mainframe()
        else:
            messagebox.showinfo("Error", "Invalid Input: Wrong username or password, please try again!", icon="error")

    def visitUs(self, event):
        webbrowser.open_new_tab("https://github.com/Gurkengewuerz/prestashop-bot")

Application()