from tkinter import *
import tkinter.ttk as tkrttk

screen = Tk()
screen.geometry("450x200")

treetime = tkrttk.Treeview(screen)

treetime["columns"] = ("Column 2", "Column 3", "Column 4", "Column 5")

treetime.column('#0', width=250, minwidth=25, stretch=NO)
treetime.column('Column 2', width=50, minwidth=25, stretch=NO)
treetime.column('Column 3', width=50, minwidth=25, stretch=NO)
treetime.column('Column 4', width=50, minwidth=25, stretch=NO)
treetime.column('Column 5', width=50, minwidth=25, stretch=NO)

treetime.heading("#0", text="Column 1", anchor=W)
treetime.heading("Column 2", text="Column 2", anchor=W)
treetime.heading("Column 3", text="Column 3", anchor=W)
treetime.heading("Column 4", text="Column 4", anchor=W)
treetime.heading("Column 5", text="Column 5", anchor=W)

#1st LEVEL
Row1 = treetime.insert("", 1, text="First Row", values=("B1", "C1","D1","E1"))
Row2 = treetime.insert("", 2, text="Second Row", values=("B1", "C1", "D1","E1"))
#2nd LEVEL
SBL1A = treetime.insert(Row1, "end", text="SubLevel Row 1", values=("B1.1", "C1.1", "D1.1", "E1.1"))
SBL1B = treetime.insert(Row1, "end", text="SubLevel Row 2", values=("B1.2", "C1.2", "D1.2", "E1.2"))

SBL2A = treetime.insert(Row2, "end", text="SubLevel Row 2", values=("B1.1", "C1.1", "D1.1", "E1.1"))
SBL2B = treetime.insert(Row2, "end", text="SubLevel Row 2", values=("B1.2", "C1.2", "D1.2", "E1.2"))



#======ADD PICTURES==========================
logo = PhotoImage(file='BSlogo512.gif').subsample(20, 20)
SBL1C = treetime.insert(Row1, "end", 'pic', text="SubLevel Row 3", image=logo, values=("B1.3", "C1.3", "D1.3", "E1.3"))


treetime.pack(side=TOP, fill=X)


screen.mainloop()


