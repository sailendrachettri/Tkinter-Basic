from tkinter import *

root = Tk()
root.title("CHECK-BOXES")
root.geometry("400x400")

def getvals():
    print("Its Worked!")

Label(root, text="Welcome to Harry Studio", font="comicsansms 10 bold").grid(row=0, column=3)

name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
payment = Label(root, text="Payment Mode")
emergency = Label(root, text="Emergency Contact")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
payment.grid(row=4, column=2)
emergency.grid(row=5, column=2)

namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
paymentvalue = StringVar()
emergencyvalue = StringVar()
foodservicevalue = IntVar()

nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=paymentvalue)
paymententry = Entry(root, textvariable=emergencyvalue)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymententry.grid(row=5, column=3)

#Check Button
foodservice = Checkbutton(text="Want to prebook your meal?", variable=foodservicevalue)
foodservice.grid(row=6, column=3)

#Button
Button(text="Sumbit", command=getvals).grid(row=7, column=3)

root.mainloop()