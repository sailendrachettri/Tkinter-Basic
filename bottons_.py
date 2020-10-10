from tkinter import *

root = Tk()
root.geometry("500x500")

def hello():
    print("Print Somthing")

root.title("Buttons")
frame = Frame(root, borderwidth=4, bg="red", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame, fg="blue", text="Print Now", command=hello)
b1.pack(side=LEFT, padx=10)

b2 = Button(frame, fg="blue", text="Print Now")
b2.pack(side=LEFT, padx=10)

b3 = Button(frame, fg="blue", text="Print Now")
b3.pack(side=LEFT, padx=10)

b4 = Button(frame, fg="blue", text="Print Now")
b4.pack(side=LEFT, padx=10)


root.mainloop()
