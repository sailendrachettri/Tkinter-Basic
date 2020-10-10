from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title("Radio Button Tutorial")
root.geometry("500x500")

def order():
    tmsg.showinfo("Order received!", f"We have received your order '{var.get()}'. Thanks for ordering.")

var = StringVar()
var.set("Radio")
Label(root, text="What would you like to have sir?",
      justify=LEFT, padx=4, font="lucida 20 bold").pack()

radio = Radiobutton(root, text="Dosa", padx=4, variable=var, value="Dosa").pack(anchor="w")
radio = Radiobutton(root, text="Idly", padx=4, variable=var, value="Idly").pack(anchor="w")
radio = Radiobutton(root, text="Somasha", padx=4, variable=var, value="Somasha").pack(anchor="w")
radio = Radiobutton(root, text="Paratha", padx=4, variable=var, value="Paratha").pack(anchor="w")

Button(root, text="Order Now", command=order).pack()
root.mainloop()