import tkinter as tk
from tkinter import *
from tkinter import messagebox
root = tk.Tk()
root.title('tk')
root.configure(background='lightgrey')
root.geometry('500x300')
L1 = Label(root,text="Full Name")
L1.grid(row=1,column=1,padx=5,pady=5)
E1 = Entry(root,width=30)
E1.grid(row=1 ,column=3,padx=5,pady=5)
L1 = Label(root,text="Email")
L1.grid(row=2,column=1,padx=5,pady=5)
E1 = Entry(root,width=30)
E1.grid(row=2 ,column=3,padx=5,pady=5)
L1 = Label(root,text="Password")
L1.grid(row=3,column=1,padx=5,pady=5)
E1 = Entry(root,width=30,show="*")
E1.grid(row=3 ,column=3,padx=5,pady=5)
L2 = Label(root,text="Gender")
L2.grid(row=4,column=1,padx=5,pady=5)
Cas = IntVar()
R1 = Radiobutton(root,text="Male",value=1,variable=Cas)
R2 = Radiobutton(root,text="Female",value=2,variable=Cas)
R3 = Radiobutton(root,text="Others",value=3,variable=Cas)
R1.grid(row=4,column=3,padx=5,pady=5)
R2.grid(row=5,column=3,padx=5,pady=5)
R3.grid(row=6,column=3,padx=5,pady=5)
C1 = Checkbutton(root,text="Accept the terms & conditions")
C1.grid(row=7,column=3,padx=5,pady=5)
B1 = Button(root,width=20,padx=2,pady=2,text="Submit")
B1.grid(row=8,column=3,padx=5,pady=5)
root.mainloop()
