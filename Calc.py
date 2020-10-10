'''
Author: Sailendra Chettri
Purpose: Calculator
Date:19/09/2020
'''

from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("300x610")
root.minsize(300, 610)
root.maxsize(300, 610)

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)

    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error!"

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("") 
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar=scvalue, font="lucida 30 bold")
screen.pack(fill=X, ipadx=5, padx=10, pady=10)

f = Frame(root, bg="gray")
f.pack()

b = Button(f, text="9", font="lucida 29 bold")
b.pack(side=LEFT, padx=15, pady=15)
b.bind('<Button-1>', click)

b = Button(f, text="8", font="lucida 29 bold")
b.pack(side=LEFT, padx=15, pady=10)
b.bind('<Button-1>', click)

b = Button(f, text="7", font="lucida 29 bold")
b.pack(side=LEFT, padx=15, pady=10)
b.bind('<Button-1>', click)

f = Frame(root, bg="gray")
f.pack()

b = Button(f, text="6", font="lucida 29 bold")
b.pack(side=LEFT, padx=15, pady=10)
b.bind('<Button-1>', click)

b = Button(f, text="5", font="lucida 29 bold")
b.pack(side=LEFT, padx=15, pady=10)
b.bind('<Button-1>', click)

b = Button(f, text="4", font="lucida 29 bold")
b.pack(side=LEFT, padx=15, pady=10)
b.bind('<Button-1>', click)

f = Frame(root, bg="gray")
f.pack()

b = Button(f, text="3", font="lucida 29 bold")
b.pack(side=LEFT, padx=15, pady=10)
b.bind('<Button-1>', click)

b = Button(f, text="2", font="lucida 29 bold")
b.pack(side=LEFT, padx=15, pady=10)
b.bind('<Button-1>', click)

b = Button(f, text="1", font="lucida 29 bold")
b.pack(side=LEFT, padx=15, pady=10)
b.bind('<Button-1>', click)

f = Frame(root, bg="gray")
f.pack()

b = Button(f, text="0", font="lucida 29 bold", padx=18)
b.pack(side=LEFT, padx=10, pady=10)
b.bind('<Button-1>', click)

b = Button(f, text="-", font="lucida 29 bold", padx=16)
b.pack(side=LEFT, padx=15, pady=10)
b.bind('<Button-1>', click)

b = Button(f, text="/", font="lucida 29 bold", padx=16)
b.pack(side=LEFT, padx=15, pady=10)
b.bind('<Button-1>', click)

f = Frame(root, bg="gray")
f.pack()

b = Button(f, text="*", font="lucida 29 bold")
b.pack(side=LEFT, padx=15, pady=10)
b.bind('<Button-1>', click)

b = Button(f, text="%", font="lucida 29 bold")
b.pack(side=LEFT, padx=10, pady=10)
b.bind('<Button-1>', click)

b = Button(f, text="+", font="lucida 29 bold")
b.pack(side=LEFT, padx=15, pady=10)
b.bind('<Button-1>', click)

f = Frame(root, bg="gray")
f.pack()

b = Button(f, text="=", font="lucida 29 bold")
b.pack(side=LEFT, padx=12, pady=10)
b.bind('<Button-1>', click)

b = Button(f, text="C", font="lucida 29 bold")
b.pack(side=LEFT, padx=15, pady=10)
b.bind('<Button-1>', click)

b = Button(f, text=".", font="lucida 29 bold")
b.pack(side=LEFT, padx=21, pady=10)
b.bind('<Button-1>', click)

root.mainloop()