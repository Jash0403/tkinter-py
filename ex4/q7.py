from cgitb import text
from msilib.schema import CheckBox
from tkinter import *
from tkinter.tix import COLUMN

root = Tk()
root.geometry("500x400")

l1 = Label(text="contact list")
l1.grid(row=0,column=0)

t = Text(width=20, height=10)
t.grid(row=1,column=0)

b1 = Button(text="Display Content")
b1.grid(row=2,column=0)

l2 = Label(text="Last name :")
l2.grid(row=3,column=0)
v1 = IntVar
E1=Entry(textvariable=v1)
E1.grid(row=3,column=1)

b2 = Button(text="Search")
b2.grid(row=4,column=0,pady=5)
l3 = Label(text="contact list").grid(row=0,column=3)
v2 = StringVar
l4 = Label(text="First Name: ").grid(row=1,column=3)
E2=Entry(textvariable=v2).grid(row=1,column=4)

l5 = Label(text="Last Name: ").grid(row=2,column=3)
E3=Entry(textvariable=v2).grid(row=2,column=4)

l6 = Label(text="Phone Number: ").grid(row=3,column=3)
E4=Entry(textvariable=v1).grid(row=3,column=4)

c = Checkbutton(text="Friend").grid(row=4,column=3)

l7 = Label(text="Email: ").grid(row=5,column=3)
E5=Entry(textvariable=v2).grid(row=5,column=4)

l8 = Label(text="Birthday: ").grid(row=6,column=3)
E6=Entry(textvariable=v1).grid(row=6,column=4)

b = Button(text="Add Contact").grid(row=7,column=3)

root.mainloop()
