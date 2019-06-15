# Project 4
# Student Information printer

from tkinter import *

def gradenter():
    print("Name: ",name.get(),"\nStudent Number:",studentno.get(),"\nCourse Code:",code.get(),"\nNumeric grade:",grade.get())
    while True:
        if grade.get() >= 90:
            print("Grade: A\n")
            return
        elif grade.get() >= 80:
            print("Grade: B\n")
            return
        elif grade.get() >=70:
            print("Grade: C\n")
            return
        elif grade.get() >=60:
            print("Grade: D\n")
            return
        else:
            print("Grade: F\n")
            return

def clearall():
    nE.delete(0, END)
    SNe.delete(0, END)
    CCe.delete(0, END)
    gE.delete(0, END)

def clearnE():
    nE.delete(0, END)
def clearSNe():
    SNe.delete(0, END)
def clearCCe():
    CCe.delete(0, END)
def cleargE():
    gE.delete(0, END)

root = Tk()
#root.geometry("232x205")

nl = Label(root, text="Name:",bg="red")
nl.grid(row=1,column=1,sticky=E)
name = StringVar()
nE = Entry(root, textvariable=name)
nE.insert(0, "")
nE.grid(row=1,column=2)
Button(root, text="Clear",bg="gray",fg="white",activebackground="lightblue",activeforeground="black",command=clearnE).grid(row=1,column=3)

SNl = Label(root, text="Student No.:",bg="red")
SNl.grid(row=2,column=1,sticky=E)
studentno = IntVar()
SNe= Entry(root, textvariable=studentno)
SNe.insert(0, " ")
SNe.grid(row=2,column=2)
Button(root, text="Clear",bg="gray",fg="white",activebackground="lightblue",activeforeground="black",command=clearSNe).grid(row=2,column=3)

CCl = Label(root, text="Cource:",bg="red")
CCl.grid(row=3,column=1,sticky=E)
code = StringVar()
CCe = Entry(root, textvariable=code)
CCe.insert(0," ")
CCe.grid(row=3,column=2)
Button(root, text="Clear",bg="gray",fg="white",activebackground="lightblue",activeforeground="black",command=clearCCe).grid(row=3,column=3)

gl = Label(root, text="Grade(%):",bg="red")
gl.grid(row=4,column=1,sticky=E)
grade = DoubleVar()
gE = Entry(root, textvariable=grade)
gE.insert(0, " ")
gE.grid(row=4,column=2)
Button(root, text="Clear",bg="gray",fg="white",activebackground="lightblue",activeforeground="black",command=cleargE).grid(row=4,column=3)

Label(root, text=" ",bg="red").grid(column=2)

Button(root, text="Clear All",bg="gray",fg="white",activebackground="lightblue",activeforeground="black",command=clearall).grid(column=2)

Button(root, text="Show result",command=gradenter).grid(column=2)

Button(root, text="Close",bd=2,bg="#A44747",fg="#B8B8E6",relief=RAISED,activebackground="red",command=root.quit).grid(column=3)

root.title("SkillUSA Problem 2012")
menu = Menu(root)
menu_file = Menu(menu)
menu_file.add_command(label="Open")
menu_file.add_command(label="Save")
menu_file.add_command(label="Save as....")
menu_file.add_separator()
menu_file.add_command(label="Exit",command=root.quit)
menu.add_cascade(label="File", menu=menu_file)
root.config(menu=menu)
root.config(bg="red")
root.mainloop()

#https://cctstaceyfornstrom.files.wordpress.com/2015/01/skillsusa_computerprogramming2012.pdf
