from tkinter import *

root = Tk()
root.title("EVENTS IN TKINTER")
root.geometry("500x400")

def harry(event):
    print(f"Button Clicked! {event.x}, {event.y}")

widget = Button(root, text="Click Me Please!")
widget.pack()

widget.bind('<Button-1>', harry)
widget.bind('<Double-1>', quit)
root.mainloop()
