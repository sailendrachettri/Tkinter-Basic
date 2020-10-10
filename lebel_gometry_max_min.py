from tkinter import *

root = Tk()
# 733 434
# width x height
root.geometry("704x300")

# width, height
root.minsize(200,200)

# width, height
root.maxsize(300, 300)

labels = Label(text="This is a Lable")
labels.pack()

root.mainloop()