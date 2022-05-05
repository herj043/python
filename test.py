from tkinter import *
from research import *


def cry():
    print("*crying*")

def loop_win():
    for i in range(4):
        print("window loop (" + str(i+1) + "/4)")
        myLabel = Label(Tk(), text="Hello World")

        myLabel.pack()
        
        Tk().mainloop()
    
print("Program running")

if k == 1:
    leave = input("do you wish to to deal with looping windows?  ")


    if "end" in leave.lower():
        print("Exiting program...")
        exit()
    elif "y" in leave.lower():
        print("looping windows...")
        loop_win()

print("Program end")