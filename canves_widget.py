from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.title("Canvas Widget")
root.geometry(f"{canvas_width}x{canvas_height}")
can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

#The line goes from the point x1, y1 to x2, y2
# can_widget.create_line(0, 0, 800, 400, fill="blue")
# can_widget.create_line(0, 400, 800, 0, fill="blue")

#To create a rectangle: coordinates of top left & coordinates of bottom left
# can_widget.create_rectangle(3, 4, 300, 200, fill="red")

#Create Text
# can_widget.create_text(300, 300, text="Some Text")
#
# can_widget.create_oval(111,222,311,114)

can_widget.winfo_screen()
root.mainloop()
