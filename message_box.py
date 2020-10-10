'''
Author: Sailendra
Date:18/09/2020
'''

from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title("Menu and Submenu")
root.geometry("500x500")

def func1():
    print("Creating Menu Using Tkinter!")

def help():
    print("Help Function!")
    tmsg.showinfo("Help", "Harry will help you!")

def rate():
    print("Rate Us!")
    val = tmsg.askquestion("How was you experience", "Was your experience Good?")
    if val == "yes":
        msg = "Great. Rate us on Appstore Please!"

    else:
        msg = "Tell us what went wrong. we will call you soon."
    tmsg.showinfo("Experience", msg)

def  deviya():
    ans = tmsg.askretrycancel("Be my Friend", "I'm Sorry I am not interested!")
    if ans:
        print("Nothing happened when retry!")
    else:
        print("Cncel It!")

mainmenu = Menu(root)

#-----------------------------------FIRST MENU-----------------------------------------------------
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New Project", command=func1)
m1.add_command(label="Save", command=func1)
m1.add_separator()
m1.add_command(label="Save As", command=func1)
m1.add_command(label="Print", command=func1)
m1.add_command(label="Edit", command=func1)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)

#---------------------------------------SECOND MENU-------------------------------------------------
m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Undo", command=func1)
m2.add_command(label="Redo", command=func1)
m2.add_separator()
m2.add_command(label="Cut", command=func1)
m2.add_command(label="Copy", command=func1)
m2.add_command(label="Paste", command=func1)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

#----------------------------------THIRD MENU--------------------------------------------------------
m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate Us", command=rate)
m3.add_command(label="Deviya", command=deviya)
mainmenu.add_cascade(label="Help", menu=m3)
root.config(menu=mainmenu)
root.mainloop()