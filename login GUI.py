# LOGIN GUI with tkinter

from errno import E2BIG
from logging import root
from math import expm1
from os import uname
from tkinter import *
from tkinter import messagebox

from click import password_option

def ok():
    uname = e1.get()
    password = e2.get()

    if (uname == "" and password == ""):
        messagebox.showinfo("","Blank Not allowed")
    
    elif (uname =="Admin" and password == "123"):

        messagebox.showinfo("","Login success")
        root.desstroy()

    else:
        messagebox.showinfo("","Incorrrent username and password")

root = Tk()
root.title("login")
root.geometry("300x200")
global e1
global e2

Label(root,text= "UserName").place(x=10,y=10)
Label(root,text= "Password").place(x=10,y=40)

e1 =Entry(root)
e1. place(x=140,y=10)

e2 = Entry(root)
e2.place(x=140,y=40)
e2.config(show="*")

Button(root,text="login",command=ok,height=3,width=13).place(x=10,y=100)

root.mainloop()