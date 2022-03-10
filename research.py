from tkinter import *
leave = input("do you wish to shut the program down? (yes/no): ")

if "y" in leave.lower():
    print("Exiting program...")
    exit()
for i in range(4):
    myLabel = Label(Tk(), text="Hello World")

    myLabel.pack()





