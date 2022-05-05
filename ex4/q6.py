from tkinter import *

root = Tk()
root.geometry("300x300")
l1=Label(text="Annual Rate:  ")
v1 = IntVar
v2 = IntVar
v3 = IntVar
v4=IntVar
v5=IntVar

E1=Entry(textvariable=v1)
l1.grid(row=1,column=0,pady=6)
E1.grid(row=1,column=1)

l2=Label(text="Number of Payments: ")
E2=Entry(textvariable=v2)
l2.grid(row=2,column=0,pady=6)
E2.grid(row=2,column=1)

l3=Label(text="Loan Principle ")
E3=Entry(textvariable=v3)
l3.grid(row=3,column=0,pady=6)
E3.grid(row=3,column=1)



l4=Label(text="Monthly Payment ")
l4.grid(row=4,column=0,pady=6)
E4=Entry(textvariable=v4)
E4.grid(row=4,column=1)

l5=Label(text="Remainig Loan ")
l5.grid(row=5,column=0,pady=6)
E5=Entry(textvariable=v5)
E5.grid(row=5,column=1)

b1 = Button(text="Final Balance").grid(row=6,column=0)
b2 = Button(text="Monthly Payment").grid(row=6,column=1)
b3 = Button(text="Quit").grid(row=6,column=2)

root.mainloop()