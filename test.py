import tkinter as tk
import calendar as cal

root = tk.Tk()
run_gui = True

class Calendar_GUI:
    
    def __init__(self, window, word = "None", grid_row = 0, grid_column = 0):
        self.window = tk.Frame(window)
        self.window.grid()

        self.date = tk.Button(window, text=word, padx=50, pady=50)
        self.date.grid(row=grid_row, column=grid_column)

# Calendar Dates
yy = 2022
mm = 6
dd = 30
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Satuday", "Sunday"]
day = cal.weekday(yy, mm, dd)

# Number Translation
number = {1: "First", 2: "Second", 3: "Third", 4: "Fourth", 5: "Fifth", 6: "Sixth", 7: "Seventh", 8: "Eighth", 9: "Ninth", 10: "Tenth", \
        11: "Elenventh", 12: "Twelth", 13: "Thirteenth", 14: "Fourteenth", 15: "Fifteenth", 16: "Sixteenth", 17: "Seventeenth", 18: "Eighteenth", \
        19: "Nineteenth", 20: "Twentieth", 21: "Twenty-First", 22: "Twenty-Second", 23: "Twenty-Third", 24: "Twenty-Fourth", 25: "Twenty-Fifth", \
        26: "Twenty-Sixth", 27: "Twenty-Seventh", 28: "Twenty-Eighth", 29:  "Twenty-Ninth", 30: "Thirdieth", 31: "Thirdy-First"}

number_word = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth",  "Seventh", "Eighth", "Ninth", "Tenth", \
        "Elenventh", "Twelth", "Thirteenth", "Fourteenth", "Fifteenth", "Sixteenth", "Seventeenth", "Eighteenth", \
        "Nineteenth", "Twentieth", "Twenty-First", "Twenty-Second", "Twenty-Third", "Twenty-Fourth", "Twenty-Fifth", \
        "Twenty-Sixth", "Twenty-Seventh", "Twenty-Eighth", "Twenty-Ninth", "Thirdieth", "Thirdy-First"]
var = ["a", "b", "c"]


for i, item in enumerate(number):
    if i <
        row = 1 
    
    item = Calendar_GUI(root, item, i)




if run_gui == True:
    root.mainloop() 

# display the calendar
print(cal.month(yy, mm))
print(str(days[day]) + ": " + str(dd))