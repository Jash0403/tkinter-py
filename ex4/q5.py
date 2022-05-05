from cgitb import text
from tkinter import *

root = Tk()
root.geometry("500x300")
l1=Label(text="Movie Booking id  ")
v1 = IntVar
v2 = StringVar
v3 = StringVar
v4=IntVar
E1=Entry(textvariable=v1)
l1.grid(row=1,column=0,pady=6)
E1.grid(row=1,column=1)

l2=Label(text="Person Name ")
E2=Entry(textvariable=v2)
l2.grid(row=2,column=0,pady=6)
E2.grid(row=2,column=1)

l3=Label(text="Movie Name ")
E3=Entry(textvariable=v3)
l3.grid(row=3,column=0,pady=6)
E3.grid(row=3,column=1,)



l4=Label(text="Class ")
l4.grid(row=4,column=0,pady=6)
radio = Radiobutton(root, text="A",value=1)
radio.grid(row=4, column=1)
radio = Radiobutton(root, text="B",value=2)
radio.grid(row=4, column=2)
Label(text="Time of show").grid(row=4, column=3)
Checkbutton(text="7.15pm").grid(row=4, column=4)
Checkbutton(text="9am").grid(row=4, column=5)

Label(text="No.of tickets").grid(row=5,column=0)
Scale(from_=1, to=6,orient=HORIZONTAL).grid(row=5,column=1,pady=6)

b1 = Button(text="Insert").grid()
b2 = Button(text="Update").grid(row=6 ,column=1)
b3 = Button(text="Delete").grid()
b4 = Button(text="Select").grid(row=7,column=1)

root.mainloop()