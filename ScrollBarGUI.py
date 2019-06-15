from tkinter import *

root = Tk()

scroll = Scrollbar(root)
scroll.grid(row=1,column=2,sticky='sn')
list1 = Listbox(root,height=10,yscrollcommand=scroll.set,bg="lightblue",fg="red",relief=FLAT)

for num in range(1,21):
    list1.insert(END, "Number: " + str(num))

list1.grid(row=1,column=1)

root.title("")
scroll.config(command=list1.yview,relief=FLAT)
root.mainloop()
