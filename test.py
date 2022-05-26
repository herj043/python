import tkinter as tk
import calendar as cal


# tkinter gui object
root = tk.Tk()
run_gui = True


# Calendar Dates
yy = 2022
mm = 5
first_day = 1

week_day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Satuday", "Sunday"]
month_names = [" ", "January", "February", "March", "April", "May", "June", "July", \
            "August", "September", "October", "November", "December"]
day = cal.weekday(yy, mm, first_day)


# Number Dictionary
number_word = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth",  "Seventh", "Eighth", "Ninth", "Tenth", \
        "Elenventh", "Twelth", "Thirteenth", "Fourteenth", "Fifteenth", "Sixteenth", "Seventeenth", "Eighteenth", \
        "Nineteenth", "Twentieth", "Twenty-First", "Twenty-Second", "Twenty-Third", "Twenty-Fourth", "Twenty-Fifth", \
        "Twenty-Sixth", "Twenty-Seventh", "Twenty-Eighth", "Twenty-Ninth", "Thirdieth", "Thirdy-First"]


# Date calendar
class Calendar_Date_GUI:
    
    def __init__(self, parent, title = "None",  word = "None", grid_row = 0, grid_column = 0):
        self.parent = parent


        self.grid_row = grid_row
        self.grid_column = grid_column

        self.word = word
        self.title = title

    def update_gui(self):
        self.window = tk.Frame(self.parent)
        self.window.grid()

        self.date = tk.Button(self.parent, text=self.word, padx=20, pady=15)
        self.date.grid(row=self.grid_row, column=self.grid_column, sticky="nesw")

    def __repr__(self):
        return str(self.title)


class Calendar_Name_GUI:
    
    def __init__(self, parent, word = "None", grid_row = 0, grid_column = 0):
        self.parent = parent

        self.grid_row = grid_row
        self.grid_column = grid_column

        self.word = word
        self.font_size = 10
        self.column_span = 1

    def update_gui(self):
        self.window = tk.Frame(self.parent)
        self.window.grid()

        self.date = tk.Label(self.parent, text=self.word, font=("Arial", self.font_size))
        self.date.grid(row=self.grid_row, column=self.grid_column, sticky="nesw", columnspan=self.column_span)
    
    def __repr__(self):
        return self.word


# Finds the last day of the month and returns it
def get_month_last_date():
    last_day = 31
    while True:
        try:
            month = cal.weekday(yy,mm, last_day)
            return last_day
        except:
            last_day += -1 


# Creates Calendar GUI 
def create_calendar_gui(window):

    date_column = day
    last_day_month = get_month_last_date()
    date_row = 2

    # Calendar Month
    month = Calendar_Name_GUI(window, month_names[mm] + " " + str(yy), 0, 0)
    month.font_size = 20
    month.column_span = 7
    month.update_gui()

    # Calendar Weekday
    for i,item in enumerate(week_day_names):
        item = Calendar_Name_GUI(window, item[0:3], date_row - 1, i)
        item.update_gui()

    # Calendar Dates
    for i in range(last_day_month):
        number_word[i] = Calendar_Date_GUI(window, number_word[i], i + 1, date_row, date_column)
        number_word[i].update_gui()

        date_column += 1
        if  date_column >= 7:
            date_row += 1 
            date_column += -7


##### Testing Puposes #####
if run_gui == True:
    create_calendar_gui(root)
    root.mainloop() 

# display the calendar
print(cal.month(yy, mm))
print(str(week_day_names[day]) + ": " + str(first_day))
