# Project 3
# Currency Converter

from tkinter import *

def printconvert():
    print("USD: ",M.get(),"\nBritish Pound: ",M.get()*0.64,"\nFrench francs: ",M.get()*6.07426,"\nItalian lire: ",M.get()*1793.62,"\nGerman Deutsche mark: ",M.get()*1.811,"\nSpanish pesetas: ",M.get()*154.076,"\n")

def clearEntry():
    Me.delete(0, END)

root = Tk()
root.geometry("250x180")

hd = Label(root, text="Convert USD\nTo\nPound, Francis, Lire, \nDeutshche mark, Pesetas",bg="white",fg="black")
hd.grid(column=2)

Label(root, text=" ").grid(column=1)

Ml = Label(root, text="Enter USD:", bg="lightblue",fg="green")
Ml.grid(row=2,column=1,sticky=E)
M = DoubleVar()
Me = Entry(root, textvariable=M, bg="red",fg="white")
Me.grid(row=2,column=2)

Cvt = Button(root, text="Convert",bd=5, bg="blue",fg="red",activebackground="red",activeforeground="blue",command=printconvert)
Cvt.grid(column=2)

clearbtn = Button(root, text="Clear",bg="white",fg="blue",activebackground="red",activeforeground="black",command=clearEntry)
clearbtn.grid(row=2,column=3)

quitbtn = Button(root, text="Quit",bg="gray",fg="white",activebackground="red",activeforeground="black",command=root.quit)
quitbtn.grid(column=2)

root.title("Converter:")
root.mainloop()
