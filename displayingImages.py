from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("455x244")
# photo = PhotoImage(file="img.png") # Only Hndles PNG images

image = Image.open("img.jpg")
photo = ImageTk.PhotoImage(image)
label = Label(image=photo)
label.pack()

root.mainloop()