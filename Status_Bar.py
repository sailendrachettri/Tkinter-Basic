'''
Author: Sailendra Chettri
Purpose: Status Bar
Date:20/09/2020
'''

from tkinter import *

root = Tk()
root.title("Status Bar")
root.geometry("500x500")

def upload():
    statusvar.set("Busy...")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready Now")
statusvar = StringVar()
statusvar.set("Ready")

sbar = Label(root, textvariable=statusvar, relief=SUNKEN, anchor=W)
sbar.pack(side=BOTTOM, fill=X)
Button(root, text="Upload", command=upload).pack()
root.mainloop()