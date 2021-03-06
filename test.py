from glob import glob
import tkinter as tk
import calendar as cal

#########################################################################################################
#########################################################################################################
#########################################################################################################

# Button commands to switch months
class Calendar_Month_Switch:

    def __init__(self, parent, title = "None",  word = "None", grid_row = 0, grid_column = 0, value = 0):
        self.parent = parent
        self.value = value

        self.grid_row = grid_row
        self.grid_column = grid_column

        self.word = word
        self.title = title

    def update_gui(self):

        self.date = tk.Button(self.parent, text=self.word, padx=10, pady=5, border=1, \
                             command=lambda: month_change(self.value, self.parent))
        self.date.grid(row=self.grid_row, column=self.grid_column,)

    def __repr__(self):
        return str(self.title)

# Days of the calender   EX: 1, 2, 3, 4
class Calendar_Date_GUI:
    
    def __init__(self, parent, title = "None",  word = "None", grid_row = 0, grid_column = 0):
        self.parent = parent

        self.grid_row = grid_row
        self.grid_column = grid_column

        self.word = word
        self.title = title

    def update_gui(self):
        self.date = tk.Button(self.parent, text=self.word, padx=20, pady=15, command= self.destroy_gui)
        self.date.grid(row=self.grid_row, column=self.grid_column, sticky="nesw")

    def destroy_gui(self):
        self.date.destroy()

    def __repr__(self):
        return str(self.title)

# Names of the days   EX: June 2022, Thursday, Friday.
class Calendar_Name_GUI:
    
    def __init__(self, parent, word = "None", grid_row = 0, grid_column = 0):
        self.parent = parent

        self.grid_row = grid_row
        self.grid_column = grid_column

        self.word = word
        self.font_size = 10
        self.column_span = 1

    def update_gui(self):

        self.date = tk.Label(self.parent, text=self.word, font=("Arial", self.font_size))
        self.date.grid(row=self.grid_row, column=self.grid_column, sticky="nesw", columnspan=self.column_span)
    
    def __repr__(self):
        return self.word

#########################################################################################################
#########################################################################################################
#########################################################################################################

# Finds the last day of the month and returns it
def get_month_last_date(month, year):
    last_day = 31
    while True:
        try:
            month = cal.weekday(year, month, last_day)
            return last_day
        except:
            last_day += -1 

# Changes the month variables and updates calendar GUI
def month_change(value, parent):
    global user_month_pick
    global user_year_date

    clean_gui()
    user_month_pick += value

    if (mm + user_month_pick) == 0:
        user_month_pick += 12
        user_year_date += -1

    if (mm + user_month_pick) == 13:
        user_month_pick += -12
        user_year_date += 1

    day = cal.weekday(user_year_date + yy, mm + user_month_pick, 1)

    create_calendar_gui(parent, mm + user_month_pick, yy + user_year_date, day)

# wipes out previous GUI dates to conserve performance
def clean_gui():
    for i in range(len(number_word)):
        try:
            number_word[i].destroy_gui()
        except:
            continue


# Creates Calendar GUI 
def create_calendar_gui(parent, month, year, first_day):
    global number_word

    date_column = first_day
    last_day_month = get_month_last_date(month, year)
    date_row = 2

    # Calendar Month
    month = Calendar_Name_GUI(parent, month_names[month] + " " + str(year), 0, 0)
    month.font_size = 20
    month.column_span = 7
    month.update_gui()

    # Calendar Month Switch Buttons
    back_month = Calendar_Month_Switch(parent, "Back", "<", 0, 0, -1)
    back_month.update_gui()
    
    next_month = Calendar_Month_Switch(parent, "Next", ">", 0, 6, 1)
    next_month.update_gui()
    
    # Calendar Weekday
    for i,item in enumerate(week_day_names):
        item = Calendar_Name_GUI(parent, item[0:3], date_row - 1, i)
        item.update_gui()

    # Calendar Dates
    for i in range(last_day_month):
        number_word[i] = Calendar_Date_GUI(parent, number_word[i], i + 1, date_row, date_column)
        number_word[i].update_gui()

        date_column += 1
        if  date_column >= 7:
            date_row += 1
            date_column += -7
    

#########################################################################################################
#########################################################################################################
#########################################################################################################

# tkinter gui object
root = tk.Tk()
run_gui = True
run_print_test = False


# User Interation
user_month_pick = 0
user_year_date = 0

# Calendar Dates
yy = 2022
mm = 5

# Day Names
week_day_names = [ "Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Satuday"]
month_names = [" ", "January", "February", "March", "April", "May", "June", "July", \
            "August", "September", "October", "November", "December"]
day = cal.weekday(yy, mm, 2)



# Number Dictionary
number_word = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth",  "Seventh", "Eighth", "Ninth", "Tenth", \
        "Elenventh", "Twelth", "Thirteenth", "Fourteenth", "Fifteenth", "Sixteenth", "Seventeenth", "Eighteenth", \
        "Nineteenth", "Twentieth", "Twenty-First", "Twenty-Second", "Twenty-Third", "Twenty-Fourth", "Twenty-Fifth", \
        "Twenty-Sixth", "Twenty-Seventh", "Twenty-Eighth", "Twenty-Ninth", "Thirdieth", "Thirdy-First"]

#########################################################################################################
#########################################################################################################
#########################################################################################################

##### Testing Puposes #####
if run_gui == True:
    create_calendar_gui(root, mm, yy, day)
    root.resizable(False, False)
    root.mainloop() 


# display the calendar
if run_print_test == True:
    user_input = input("'-': to move back a month, '+': to move forward a month.  Enter: ")
    user_month_base = 0
    user_year_base = 0


    while user_input != "":
        if user_input == "-":
            user_month_base += -1

        elif user_input == "+": 
            user_month_base += 1
        
        if (mm + user_month_base) == 0:
            user_month_base += 12
            user_year_base += -1

        if (mm + user_month_base) == 13:
            user_month_base += -12
            user_year_base += 1

        print(cal.month(yy + user_year_base, mm + user_month_base))
        user_input = input("'-': to move back a month, '+': to move forward a month.  Enter: ")


print(cal.month(yy, mm))
print(str(week_day_names[day]) + ": " + str(day))