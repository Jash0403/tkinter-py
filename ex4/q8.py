from tkinter import*
r=Tk()
r.title('Registration Form')
r.geometry('400x500')
l=Label(text='Form',bg='light green')
l.pack(anchor=CENTER)
r['bg']='light green'

l1=Label(r,text='Name',bg='light green').place(x=50,y=50)
l2=Label(r,text='Course',bg='light green').place(x=50,y=100)
l3=Label(r,text='Semester',bg='light green').place(x=50,y=150)
l4=Label(r,text='Form No',bg='light green').place(x=50,y=200)
l5=Label(r,text='Contact No',bg='light green').place(x=50,y=250)
l6=Label(r,text='Email Id',bg='light green').place(x=50,y=300)
l7=Label(r,text='Address',bg='light green').place(x=50,y=350)


ev1=StringVar
ev1=Entry(r,textvariable=ev1).place(x=150,y=50)
ev2=StringVar
ev2=Entry(r,textvariable=ev2).place(x=150,y=100)
ev3=StringVar
ev3=Entry(r,textvariable=ev3).place(x=150,y=150)
ev4=IntVar
ev4=Entry(r,textvariable=ev4).place(x=150,y=200)
ev5=IntVar
ev5=Entry(r,textvariable=ev5).place(x=150,y=250)
ev6=StringVar
ev6=Entry(r,textvariable=ev6).place(x=150,y=300)
ev7=StringVar
ev7=Entry(r,textvariable=ev7).place(x=150,y=350)

b1=Button(r,text='Submit',bg='red').place(x=150,y=400)
r.mainloop()