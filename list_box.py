'''
Author: Sailendra Chettri
Purpose: List Box
Date:20/09/2020
'''

from tkinter import *

root = Tk()
root.title("List Box in Tkinter")
root.geometry("500x500")

def add():
    global i
    lbx.insert(ACTIVE, f"{i}")
    i += 1
i = 0

lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First item of a list box")

Button(root, text="Add item", command=add).pack()

root.mainloop()