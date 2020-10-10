'''
Author: Sailendra Chettri
Purpose: Scroll Bar
Date:20/09/2020
'''

from tkinter import *

root = Tk()
root.title("SCROLL BAR")
root.geometry("500x500")

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root, yscrollcommand = scrollbar.set)
for i in range(400):
    listbox.insert(END, f"ITEM {i}")
listbox.pack(fill="both")
scrollbar.config(command=listbox.yview)

# text = Text(root, yscrollcommand = scrollbar.set) 
# text.pack(fill=BOTH)
# scrollbar.config(command=text.yview)

root.mainloop()