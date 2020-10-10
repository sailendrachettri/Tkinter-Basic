'''
Author: Sailendra
Date: 18/09/2020
Purpose: Slider in Tkinter
'''

from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.title("Slider in Tkinter")
root.geometry("500x500")

#=================================FUNCTIONS=============================================
def getdollor():
    print(f"We have credited {myslider2.get()} dollor to your account.")
    tmsg.showinfo("Amount created",f"We have credited {myslider2.get()} dollor to your account.")

# myslider = Scale(root, from_=0, to=100)
# myslider.pack()

Label(root, text="How many Dollors you want?").pack()
myslider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=5)
myslider2.set(30) # Set Default value
myslider2.pack()

Button(root, text="Get Dollors!", command=getdollor).pack()

root.mainloop()