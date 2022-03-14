from tkinter import *

def cry():
    print("*crying*")

def loop_win():
    for i in range(4):
        print("window loop (" + str(i+1) + "/4)")
        myLabel = Label(Tk(), text="Hello World")

        myLabel.pack()
        
        Tk().mainloop()
    