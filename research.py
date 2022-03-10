#exiting program in middle of code - in order to shut down loops (Undiscovered)


from tkinter import *
import test as t
t.cry()
leave = input("do you wish to to deal with looping windows?  ")

def loop_win():
    for i in range(4):
        print("window loop (" + str(i+1) + "/4)")
        myLabel = Label(Tk(), text="Hello World")

        myLabel.pack()
        
        Tk().mainloop()
    

if "end" in leave.lower():
    print("Exiting program...")
    exit()
elif "y" in leave.lower():
    print("looping windows...")
    loop_win()

#Spams windows after you deleted the window


root = Tk()

for i in range(4):
    myLabel = Label(root, text="Hello World")

    myLabel.pack()
root.config(background="#333333")
#Setting root.mainloop in loop then deleting breaks it also only includes "Hello World"    
root.mainloop()
exit()


