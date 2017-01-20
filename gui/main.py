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

        self.loggedIn = Label(self.main, text="Logged as %s" % userVar)
        self.loggedIn.place(x=630, y=16)

        self.commLb = Label(self.main, text="Command")
        self.commLb.place(x=5, y=413)

        self.addImg = PhotoImage(file="./img/add.png")
        self.addBtn = Button(self.main, height=20, width=35, image=self.addImg)
        self.addBtn.place(x=5, y=387)

        self.delImg = PhotoImage(file="./img/delete.png")
        self.delBtn = Button(self.main, height=20, width=35, image=self.delImg)
        self.delBtn.place(x=50, y=387)

        self.editImg = PhotoImage(file="./img/edit.png")
        self.editBtn = Button(self.main, height=20, width=35, image=self.editImg)
        self.editBtn.place(x=95, y=387)

        self.relImg = PhotoImage(file="./img/reload.png")
        self.relBtn = Button(self.main, height=20, width=35, image=self.relImg)
        self.relBtn.place(x=688, y=387)

        self.exeTb = Text(self.main, width=60, height=1)
        self.exeTb.place(x=5, y=430)

        self.statusbar = Label(self.main, text="...", bd=1, relief=SUNKEN, anchor=W)
        self.statusbar.pack(side=BOTTOM, fill=X)

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
        custOutput.pack()

        ordOutput = Text(page2, width=90, height=20)
        # ScrollBarY = Scrollbar(output)
        # ScrollBarY.config(command=output.yview)
        # ScrollBarY.pack(side=RIGHT, fill=Y)
        # output.configure(yscrollcommand=ScrollBarY.set)
        ordOutput.pack()

        prodOutput = Text(page3, width=90, height=20)
        # ScrollBarY = Scrollbar(output)
        # ScrollBarY.config(command=output.yview)
        # ScrollBarY.pack(side=RIGHT, fill=Y)
        # output.configure(yscrollcommand=ScrollBarY.set)
        prodOutput.pack()

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

        # Order Query
        ordQuery = db.query("SELECT * FROM ps_orders")
        ordQueryFetch = ordQuery.fetchall()
        for row in ordQueryFetch:
            ordOutput.insert(INSERT, "%s\t%s\t\t%s\t\t\t%s\n" % (row[0], row[1], row[2], row[3]))

        # Product Query
        prodQuery = db.query("SELECT * FROM ps_product")
        prodQueryFetch = prodQuery.fetchall()
        for row in prodQueryFetch:
            prodOutput.insert(INSERT, "%s\t%s\t\t%s\t\t\t%s\n" % (row[0], row[1], row[2], row[3]))

        # Licence Query
        licQuery = db.query("SELECT * FROM ita_licencekey")
        licQueryFetch = licQuery.fetchall()
        for row in licQueryFetch:
            licOutput.insert(INSERT, "%s\t%s\t\t%s\t\t\t%s\t\t%s\t\t\n" % (row[0], row[1], row[2], row[3], row[4]))

        self.main.mainloop()

if __name__ == "__main__":
    Mainframe()
