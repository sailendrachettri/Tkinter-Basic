from tkinter import *

root =Tk()

root.geometry("644x399")
root.title("Learning Frames")
f1 = Frame(root, bg="red", borderwidth=3, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y)

f2 = Frame(root, bg="red", borderwidth=4, relief=SUNKEN)
f2.pack(side=TOP, fill=X)

l = Label(f1, text="Harry Project")
l.pack(pady=100)

l = Label(f2, text="Welcome to Harry Text Editor")
l.pack()

root.mainloop()