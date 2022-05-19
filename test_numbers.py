from tkinter import *

win = Tk()

c = Entry(width= 80)
c.insert(0, "Insert word")

def click():
    hello = Label(win, text=c.get())
    hello.pack()
    c.delete(0, END)

def character_insert(character):
    current = c.get()
    c.delete(0, END)
    c.insert(0, str(current) + str(character))

def clear():
    c.delete(0, END)

a = Button(win, text="Hello", padx=19, pady=39, command=click)
b = Button(win, text="Clear", command=clear)
d = Button(win, text="_", command=lambda:character_insert("________________________________"))

b.pack()
c.pack()
a.pack()
d.pack()
win.mainloop()



a = {}
print(type(a))