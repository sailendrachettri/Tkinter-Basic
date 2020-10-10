from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("Harry GUI")

# ----------Important Label Options------------------
''' 
text =  adds the text
bg = background
fg = foreground
font = set the font
 i. font=("fontname", 20, "bold")
 ii. font="fontname 20 bold"
padx = x padding
pady = y padding
relief = border styling --> SUNKEN, RAISED, GROOVE, RIDGE
'''

label_text = Label(text=''' Arjuna is depicted as a skilled archer and wins the hand\n of Draupadi in marriage. She becomes his first wife and \n is simultaneously married to Arjuna's brothers. \n He is twice exiled, first for breaking a pact with his \n brothers; and secondly together with them when his\n oldest brother is tricked into gambling away the throne. \n Some notable incidents during the first exile were \nArjuna's involvement in the burning of the Khandava Forest \n and his marriages with Ulupi, Chitrāngadā and Subhadra. \nIn the Kurukshetra War, Lord Krishna became his \n charioteer and taught him the sacred knowledge of Gita.''', bg="red", fg="blue", padx=20, pady=20, font="random 10 bold", borderwidth=4, relief=SUNKEN)
label_text.pack(side="bottom", anchor="sw", fill=X)

# ----------Important Pack Options------------------
'''
anchor = nw
side = top, left, right, bottom
fill = X or Y 
padx = 
pady = 
'''
root.mainloop()