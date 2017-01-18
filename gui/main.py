from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import *
import time
from tkinter.scrolledtext import ScrolledText
# from login import *
import sys

db = DB()


class Mainframe:
    def __init__(self, userVar):
        self.main = Toplevel()
        self.main.iconbitmap(default="./img./ico.ico")
        self.main.title("Administration Control Panel")
        self.main.resizable(width=FALSE, height=FALSE)
        self.main.geometry("800x480")

        self.defUser = PhotoImage(file="./img/default_user.png")
        self.defUserLb = Label(self.main, image=self.defUser).place(x=735, y=12)

        self.loggedIn = Label(self.main, text="Welcome, %s" % userVar)
        self.loggedIn.place(x=635, y=20)

        self.commLb = Label(self.main, text="Command")
        self.commLb.place(x=5, y=413)

        self.exeTb = Text(self.main, width=60, height=1)
        self.exeTb.place(x=5, y=430)

        tab = ttk.Notebook(self.main)

        page1 = ttk.Frame(tab)
        page2 = ttk.Frame(tab)
        page3 = ttk.Frame(tab)
        page4 = ttk.Frame(tab)

        tab.add(page1, text="Customers")
        tab.add(page2, text="Orders")
        tab.add(page3, text="Products")
        tab.add(page4, text="Licences")
        tab.place(x=3, y=35)

        custOutput = Text(page1, width=90, height=20)
        # ScrollBarY = Scrollbar(output)
        # ScrollBarY.config(command=output.yview)
        # ScrollBarY.pack(side=RIGHT, fill=Y)
        # output.configure(yscrollcommand=ScrollBarY.set)
        custOutput.pack()

        licOutput = Text(page4, width=90, height=20)
        # ScrollBarY = Scrollbar(output)
        # ScrollBarY.config(command=output.yview)
        # ScrollBarY.pack(side=RIGHT, fill=Y)
        # output.configure(yscrollcommand=ScrollBarY.set)
        licOutput.pack()

        # Customer Query
        custQuery = db.query("SELECT * FROM ps_customer")
        custQueryFetch = custQuery.fetchall()
        for row in custQueryFetch:
            custOutput.insert(INSERT, "%s\t%s\t\t%s\t\t\t%s\n" % (row[0], row[10], row[11], row[12]))

        licQuery = db.query("SELECT * FROM ita_licencekey")
        licQueryFetch = licQuery.fetchall()
        for row in licQueryFetch:
            licOutput.insert(INSERT, "%s\t%s\t\t%s\t\t%s\t\t%s\t\t\n" % (row[0], row[1], row[2], row[3], row[4]))


        self.statusbar = Label(self.main, text="Waiting for actions...", bd=1, relief=SUNKEN, anchor=W)
        self.statusbar.pack(side=BOTTOM, fill=X)
        """
        notebook example
        """
        # text = ScrolledText(page2)
        # text.pack(expand=1, )

        """
        OLD
        """
        # self.outputTb = Text(self.main, width=91, height=20)
        # self.outputTb.place(x=8, y=6)

        # self.insertTb = Text(self.main, width=50, height=2)
        # self.insertTb.pack

        """
        Option Menu
        """
        # variable = StringVar(self.main)
        # variable.set("Welcome, %s"%self.userVar)

        # self.option = OptionMenu(self.main, variable, "one")
        # self.option.pack()

        self.main.mainloop()


if __name__ == "__main__":
    Mainframe()
