#!/usr/bin/env python3
import tkinter as tk
import tkinter.ttk as ttk
import collections
# from data import *

root = tk.Tk()
root.geometry("925x600")

###############################
#        Other Windows
###############################

# add_employee window
class Window_employee():
    def __init__(self):
        win1 = tk.Toplevel(root)
        win1.geometry("925x600+20+20")
        win1['bg']="#B8BBC5"
        title = tk.Label(win1, text="Add an employee",pady=50, bg="#B8BBC5")
        title.grid(row=0, column=3)
        fill_list = ["Name: ","Senior Staff: ","Unavailable Hours: ","Preferred event type: "]
        nrow = 0
        for i in range(len(fill_list)):
            tk.Label(win1, text=fill_list[i], anchor="e", width=20).grid(row=nrow+1, column=0)
            nrow += 1

        self.name_entry = tk.Entry(win1, width = 22)
        self.name_entry.grid(row=1, column=1)
        # name = name_entry.get()
        # print(name)
        availability_btn = tk.Button(win1, text="Choose Unavailability")
        availability_btn.config(width=22)
        availability_btn.grid(row=3, column=1)
        availability_btn['command']= window_calendar

        self.comboSenior = tk.ttk.Combobox(win1, values=["Y", "N"], width=22)
        self.comboSenior.grid(row=2, column=1)
        self.comboEvent = tk.ttk.Combobox(win1, values=["Art", "Music", "Theater", "Reception", "Dance", "No Preference"], width=22)
        self.comboEvent.grid(row=4, column=1)

        self.add_btn = tk.Button(win1, text="Add Employee")
        self.add_btn['command']=self.get_input
        self.add_btn.grid(row=5, column=1)

    def get_input(self):
        name=self.name_entry.get()
        senior = self.comboSenior.get()
        event = self.comboEvent.get()
        print(name,senior,event)
        return name, senior, event
   

def submit_employee(name_field):
    text = name_field.get()
    print(text)

# create calendar window 
def window_calendar():
    win_calendar = tk.Toplevel(root)
    win_calendar.geometry("560x450+20+20")
    win_calendar["bg"] = "#B8BBC5"
    title = tk.Label(win_calendar, text="Unavailability", bg="#B8BBC5",pady=50)
    title.grid(row = 0, column = 0)
    calendar = CheckGrid(win_calendar, rows=12, columns=7)
    done_btn = tk.Button(win_calendar, text="Update", command = calendar.get_checked)
    done_btn.grid(row=13, column=7)
    

class CheckGrid(object):
    ''' A grid of Checkbuttons '''
    def __init__(self, parent, rows, columns):

        rowrange = range(rows)
        colrange = range(columns)

        self.data = collections.defaultdict(list)
        self.colT = ["Sunday","Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday"]
        self.rowT = ["6-8 AM","8-10 AM","10-12 PM","12-2 PM","2-4 PM","4-6 PM","6-8 PM","8-10 PM","10-12 AM","12-2 AM","2-4 AM","4-6 AM"]

        #Create the grid labels
        for x in colrange:
            w = tk.Label(parent, text=self.colT[x])
            w.grid(row=0, column=x+1)

        for y in rowrange:
            w = tk.Label(parent, text=self.rowT[y])
            w.grid(row=y+1, column=0)

        #Create the Checkbuttons & save them for future reference
        self.grid = []
        for y in rowrange:
            row = []
            for x in colrange:
                b = tk.Checkbutton(parent)

                #Store the button's position and value as attributes
                b.pos = (y, x)
                b.var = tk.IntVar()

                #Create a callback bound to this button
                func = lambda w=b: self.check_cb(w)
                b.config(variable=b.var, command=func)
                b.grid(row=y+1, column=x+1)
                row.append(b)
            self.grid.append(row)
        # self.get_checked()

        #Track the number of on buttons in each row
        self.rowstate = rows * [0]


    def check_cb(self, button):
        ''' Checkbutton callback '''
        state = button.var.get()
        y, x = button.pos

        #Get the row containing this button
        row = self.grid[y]

        if state == 1:
            self.rowstate[y] += 1 
            for b in row:
                if b.var.get() == 0:
                    b.config(state=tk.NORMAL)
        else:
            self.rowstate[y] -= 1 
            if self.rowstate[y] == 1:
                #Enable all currently off buttons in this row
                for b in row:
                    if b.var.get() == 0:
                        b.config(state=tk.NORMAL)
        self.get_checked()

        #print y, x, state, self.rowstate[y] 

    def get_checked(self):
        ''' Make a list of the selected Groups in each row'''
        
        i = 0
        for row in self.grid:
            # self.data.append([x + 1 for x, b in enumerate(row) if b.var.get()])
            for x,b in enumerate(row):
                if b.var.get() == 1 and self.rowT[i] not in self.data[self.colT[x]]:
                    self.data[self.colT[x]].append(self.rowT[i])
            i += 1
        print(self.data)
        return self.data

# add_event window 
class Window_event():
    def __init__(self):
        win2 = tk.Toplevel(root)
        win2.geometry("920x600+20+20")
        win2['bg']="#B8BBC5"
        title = tk.Label(win2, text="Add an Event",pady=50, bg="#B8BBC5")
        title.grid(row=0, column=3)
        fill_list = ["Event Type ","Time Duration (Hour) ","Staff needed "]
        nrow = 0
        for i in range(len(fill_list)):
            tk.Label(win2, text=fill_list[i], anchor="e", width=20).grid(row=nrow+1, column=0)
            nrow += 1

        self.comboEvent = tk.ttk.Combobox(win2, values=["Art", "Music", "Theater", "Reception", "Dance", "No Preference"],width=22)
        self.comboEvent.grid(row=1, column=1)
        self.comboDuration = tk.ttk.Combobox(win2, values=[i/2 for i in range(1,11)],width=22)
        self.comboDuration.grid(row=2, column=1)
        self.comboNumStaff = tk.ttk.Combobox(win2, values=[i for i in range(1,31)],width=22)
        self.comboNumStaff.grid(row=3, column=1)

        self.add_btn = tk.Button(win2, text="Add Event")
        self.add_btn['command']=self.get_input
        self.add_btn.grid(row=4, column=1)

    def get_input(self):
        eventType=self.comboEvent.get()
        duration = self.comboDuration.get()
        numStaff = self.comboNumStaff.get()
        print(eventType, duration, numStaff)
        return eventType, duration, numStaff

# def window_event():
#     win2 = tk.Toplevel(root)
#     win2.geometry("920x600+20+20")
#     win2['bg']="#B8BBC5"
#     title = tk.Label(win2, text="Add an Event",pady=50, bg="#B8BBC5")
#     title.grid(row=0, column=3)
#     fill_list = ["Event Type ","Time Duration (Hour) ","Staff needed "]
#     nrow = 0
#     for i in range(len(fill_list)):
#         tk.Label(win2, text=fill_list[i], anchor="e", width=20).grid(row=nrow+1, column=0)
#         nrow += 1

#     comboEvent = tk.ttk.Combobox(win2, values=["Art", "Music", "Theater", "Reception", "Dance", "No Preference"],width=22)
#     comboEvent.grid(row=1, column=1)
#     comboDuration = tk.ttk.Combobox(win2, values=[i/2 for i in range(1,11)],width=22)
#     comboDuration.grid(row=2, column=1)
#     comboNumStaff = tk.ttk.Combobox(win2, values=[i for i in range(1,31)],width=22)
#     comboNumStaff.grid(row=3, column=1)

# staff event window
def window_staff():
    win3 = tk.Toplevel(root)
    win3.geometry("920x600+20+20")
    win3["bg"] = "#B8BBC5"
    title = tk.Label(win3, text="Staff an Event", bg="#B8BBC5",pady=50)
    title.pack()


###############################
#         Root Window
###############################

# create label widge
welcome_label = tk.Label(text = "Employee Schedule System", pady=50, bg="#B8BBC5")
blank1 = tk.Label(text = "Employee Schedule System", pady=50, fg="#B8BBC5", bg="#B8BBC5")
blank2 = tk.Label(text = "Employee Schedule System", pady=50, fg="#B8BBC5", bg="#B8BBC5")
blank3 = tk.Label(text = "Employee Schedule System", pady=50, fg="#B8BBC5", bg="#B8BBC5")
blank4 = tk.Label(text = "Employee Schedule System", pady=50, fg="#B8BBC5", bg="#B8BBC5")
    
# create buttons
add_employee_btn = tk.Button(text="Add an Employee", height = 6)
add_event_btn = tk.Button(text="Add an Event", height = 6)
staff_event_btn = tk.Button(text="Staff an Event", height = 6)
create_schedule_btn = tk.Button(text="Create Weekly Schedule", height = 6)
export_schedule_btn = tk.Button(text="Export Weekly Schedule", height = 6)

# change buttons size
add_employee_btn.config(width=20)
add_event_btn.config(width=20)
staff_event_btn.config(width=20)
create_schedule_btn.config(width=20)
export_schedule_btn.config(width=20)

# layout in the window
blank1.grid(row=0, column=0)
blank2.grid(row=0, column=1)
blank3.grid(row=0, column=3)
blank4.grid(row=0, column=4)
welcome_label.grid(row=0, column=2)
add_employee_btn.grid(row=1, column=0)#, command=win2)
add_event_btn.grid(row=1, column=1)
staff_event_btn.grid(row=1, column=2)
create_schedule_btn.grid(row=1, column=3)
export_schedule_btn.grid(row=1, column=4)


# click functions
add_employee_btn['command']=Window_employee
add_event_btn['command']=Window_event
staff_event_btn['command']=window_staff

root.mainloop()

    