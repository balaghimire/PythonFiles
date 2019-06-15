from tkinter import *
import random

def printname():
    print("Username: ", un.get(), "\nPassword: ", pw.get(), "\n")

root = Tk()
root.geometry("335x200")

#MENU
menubar = Menu(root)

filemenu = Menu(menubar)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

root.config(menu=menubar)
#END MENU

Label(root, text="").grid(column=1)

username = Label(root, text=" Username: ", bg="lightblue")
username.grid(row=2,column=1,sticky=E)
un = StringVar()
user = Entry(root, textvariable=un, bg="lightgreen",width=40)
user.grid(row=2,column=2)

password = Label(root, text="  Password: ", bg="lightblue")
password.grid(row=3,column=1,sticky=E)
pw = StringVar()
passwrd = Entry(root, textvariable=pw, bg="lightgreen",show="•",width=40)
passwrd.grid(row=3,column=2)

Label(root, text="").grid(column=1)

kli = Checkbutton(root, text="Keep Log in",activebackground="red",activeforeground="white")
kli.grid(column=2)

button = Button(root, text="Print out",fg="white",bg="blue",activebackground="green",activeforeground="white", command=printname)
button.grid(column=2)

quitbutton = Button(root, text=" Quit ",fg="white",bg="gray",activebackground="red",activeforeground="lightgreen", command=root.quit)
quitbutton.grid(column=2)

root.title("Log in: ")
root.mainloop()

#https://cctstaceyfornstrom.files.wordpress.com/2015/01/skillsusa_computerprogramming2012.pdf
#https://cctstaceyfornstrom.files.wordpress.com/2015/01/skillsusa_computerprogramming2010.pdf
