'''
Author: Sailendra
Date:18/09/2020
'''

from tkinter import *

root = Tk()
root.title("Menu and Submenu")
root.geometry("500x500")

def func1():
    print("Creating Menu Using Tkinter!")

# mymenu = Menu(root)
# mymenu.add_command(label="File", command=func1)
# mymenu.add_command(label="Exit", command=quit)
#
# root.config(menu=mymenu)

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



root.mainloop()