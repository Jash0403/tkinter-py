from tkinter import ttk
from tkinter import *
root = Tk()
root.title("Phone List")
root.config(bg="grey")
phone_list = ttk.Style()
tree = ttk.Treeview(root, column=("Name", "Phone"), show='headings',height=5)
def add():
    tree.insert('', 'end', values=(name.get(), phn.get()))
    name.delete(0, END)
    phn.delete(0, END)
def delete():
    selected_item = tree.selection()[0]
    tree.delete(selected_item)
def edit():
    selected_item = tree.selection()[0]
    tree.item(selected_item, values=(name.get(), phn.get()))
Label(root, text="Name").grid(row=0, column=0)
name = Entry(root)
name.grid(row=0, column=1)
Label(root, text="Phone").grid(row=1, column=0, pady=15)
phn = Entry(root)
phn.grid(row=1, column=1, pady=15)
Button(root, text="Add", command=add).grid(row=2, column=0, pady=15)
Button(root, text="Update", command=edit).grid(row=2, column=1, pady=15)
Button(root, text="Delete", command=delete).grid(row=2, column=2, pady=15)
scroll_bar = ttk.Scrollbar(root, orient="vertical",
command=tree.yview)
scroll_bar.grid(row=3, column=3, sticky="nsew", pady=15)
tree.configure(yscrollcommand=scroll_bar.set)
tree.column("#1", anchor=CENTER)
tree.heading("# 1", text="Name")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Phone")
tree.insert('', 'end', values=('Bamhart Rlaph', '683-2341'))
tree.insert('', 'end', values=('Jones Janet ', '483-5432'))
tree.insert('', 'end', values=('Meyers Chris ', '343-4349'))
tree.insert('', 'end', values=('Nelson Eric', '485-2689'))
tree.insert('', 'end', values=('Perfect Ford', '987-6543'))
tree.insert('', 'end', values=('Smith Bob', '689-1234'))
tree.insert('', 'end', values=('Smith Micheal', '689-1234'))
tree.grid(row=3, columnspan=3, pady=15)
root.mainloop()
