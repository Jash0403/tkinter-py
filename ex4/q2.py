from tkinter import *

root = Tk()
root.geometry("300x300")
l1=Label(text="CustId  ")
v1 = IntVar
v2 = StringVar
v3 = StringVar
v4=IntVar
E1=Entry(textvariable=v1)
l1.grid(row=1,column=0,pady=6)
E1.grid(row=1,column=1)

l2=Label(text="Customer Name: ")
E2=Entry(textvariable=v2)
l2.grid(row=2,column=0,pady=6)
E2.grid(row=2,column=1)

l3=Label(text="Branch ")
E3=Entry(textvariable=v3)
l3.grid(row=3,column=0,pady=6)
E3.grid(row=3,column=1,)



l4=Label(text="Account type ")
l4.grid(row=4,column=0,pady=6)
radio = Radiobutton(root, text="Savings",value=1)
radio.grid(row=4, column=1)
radio = Radiobutton(root, text="Non Savings",value=2)
radio.grid(row=4, column=2)

l5=Label(text="Amount ")
l5.grid(row=5,column=0,pady=6)
Scale(from_=1, to=100,orient=HORIZONTAL).grid(row=5,column=1)

b1 = Button(text="Insert").grid()
b2 = Button(text="Update").grid(row=6 ,column=1)
b3 = Button(text="Delete").grid()
b4 = Button(text="Select").grid(row=7,column=1)

root.mainloop()