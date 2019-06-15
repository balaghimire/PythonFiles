# First Project
# Address and a button

from tkinter import *

root = Tk()
root.geometry("400x200")
comName = Label(root, text="Company Name\n5522 Street Rd., Louisville, KY (40291)\nPhone: (123)456-7890", fg="black",bg="white")
ListOfItems = Label(root, text="List of Items:\nStoves - $130.99\nRefrigerator - $299.99\nDishwashers - $339.99\nChair - $98.99\nSofas - $168.99", fg="red", bg="lightblue")

button1= Button(root, text="Click Here")

#Shows here:
comName.grid(row=0,column=1)
button1.bind("Button-1")
button1.grid(row=1,column=1)
root.title("Project 1")
root.mainloop()
