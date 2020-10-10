'''
Author: Sailendra Chettri
Purpose: Tkinter Tips and Tricks
Date:20/09/2020
'''

from tkinter import *

root = Tk()
root.title("Tips and Tricks on Tkinter")
root.geometry("500x400")

# root.wm_iconbitmap("tkicon.ico") # If white background
root.configure(background="black")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print(f"{width}x{height}")

Button(text="Destory", command=root.destroy).pack()
root.mainloop()