from tkinter import *

def show(event):
    show.configure(text=entry.get(),fg="green")

box = Tk()

Label(box, text=" ").grid(column=1)

writelabel = Label(box, text="Write something:",fg="blue")
writelabel.grid(row=1,column=1)
entry = Entry(box, bg="lightgreen")
entry.bind("<Return>",show)
entry.grid(row=1,column=2,sticky=W)

Label(box, text="Result:",fg="Red").grid(column=1,sticky=W)
show = Label(box)
show.grid(row=3,column=2)

box.minsize(300,150)
box.title("Practice001")
box.mainloop()
