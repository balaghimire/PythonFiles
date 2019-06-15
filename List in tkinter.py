# Project 2
# GUI List in python
from tkinter import *

root = Tk()

Lb1= Listbox(root, height=3,bg="green",fg="white",relief=SUNKEN)
Lb1.grid(row=1,column=1)
Lb1.insert(END, "Chair","Sofa","TV")

Lb2= Listbox(root, height=3,width=7,bg="green",fg="lightblue",bd=2,relief=RAISED)
Lb2.grid(row=1,column=2)
Lb2.insert(END, "$29.99","$49.98","$670.99")
root.title("List of things")

root.config(bg="red")
root.mainloop()
