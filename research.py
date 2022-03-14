#exiting program in middle of code - in order to shut down loops (Undiscovered)
from tkinter import *
import test

k = 1
#Spams windows after you deleted the window

root = Tk()


my_label_1 = Label(root, text="Hello World")
my_label_2 = Label(root, text="Hello World be")

my_label_1.grid(row=0, column=0)
my_label_2.grid(row=1, column=2)

root.config(background="#333333")

#Setting root.mainloop in loop then deleting breaks it also only includes one "Hello World" line   
root.mainloop()
exit()


