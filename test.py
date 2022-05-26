import tkinter as tk
import calendar as cal

root = tk.Tk()
run_gui = True

class Calendar_GUI:
    
    def __init__(self, window, word = "None", grid_row = 0, grid_column = 0):
        self.window = tk.Frame(window)
        self.window.grid()

        self.date = tk.Button(window, text=word, padx=20, pady=15)
        self.date.grid(row=grid_row, column=grid_column, sticky="nesw")
        

# Calendar Dates
yy = 2022
mm = 7
dd = 1
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Satuday", "Sunday"]
day = cal.weekday(yy, mm, dd)

# Number Translation
number = {1: "First", 2: "Second", 3: "Third", 4: "Fourth", 5: "Fifth", 6: "Sixth", 7: "Seventh", 8: "Eighth", 9: "Ninth", 10: "Tenth", \
        11: "Elenventh", 12: "Twelth", 13: "Thirteenth", 14: "Fourteenth", 15: "Fifteenth", 16: "Sixteenth", 17: "Seventeenth", 18: "Eighteenth", \
        19: "Nineteenth", 20: "Twentieth", 21: "Twenty-First", 22: "Twenty-Second", 23: "Twenty-Third", 24: "Twenty-Fourth", 25: "Twenty-Fifth", \
        26: "Twenty-Sixth", 27: "Twenty-Seventh", 28: "Twenty-Eighth", 29:  "Twenty-Ninth", 30: "Thirdieth", 31: "Thirdy-First"}


date_column = day
date_row = 0
for i, item in enumerate(number):
    item = Calendar_GUI(root, item, date_row, date_column)
    date_column += 1
    if  date_column >= 7:
        date_row += 1 
        date_column += -7
    




if run_gui == True:
    root.mainloop() 

# display the calendar
print(cal.month(yy, mm))
print(str(days[day]) + ": " + str(dd))