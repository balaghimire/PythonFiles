from tkinter import *
import tkinter.messagebox as Tm

root = Tk()
root.geometry("450x110")
skipline = Label(root, text=" ")
theUser = Label(root, text=" Username: ", fg="lightblue",bg="darkgreen")
thePass = Label(root, text=" Password ", fg="lightgreen",bg="darkgreen")
button1 = Button(root, text="Log In",fg="red",bg="yellow")
VofUser = StringVar()
VofPass= StringVar()
User = Entry(root, textvariable=VofUser, bg="white", fg="black")
Pass = Entry(root, textvariable=VofPass, bg="white", show="#")

#Tm.showinfo("Log In:", "Wanna see Log in preview!!!")

#shows the things:
skipline.grid(row=1,column=1)
theUser.grid(row=2,column=3)
User.grid(row=2,column=4)
thePass.grid(row=2,column=6)
Pass.grid(row=2,column=7)
button1.grid(row=2,column=8)
root.title("Log In:")
root.mainloop()


#http://www.prasannatech.net/2009/05/tkinter-restricting-text-input-size.html
