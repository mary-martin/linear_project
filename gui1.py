#!/usr/bin/env python3
import tkinter as tk
import tkinter.ttk as ttk
import collections
from data import * 

#===========================
#        FUNCTIONS
#===========================

root = tk.Tk()
root.geometry("925x600")

# add_employee window

def window_employee():

    win1 = tk.Toplevel()
    win1.geometry("925x600+20+20")
    win1['bg']="#B8BBC5"
    title = tk.Label(win1, text="Add an employee",pady=50, bg="#B8BBC5")
    title.grid(row=0, column=3)
    
    # set labels 
    title = tk.Label(win1, text="Add an Employee: ", bg="#B8BBC5")
    name = tk.Label(win1, text="Name: ", bg="#B8BBC5")
    senior = tk.Label(win1, text="Senior Staff: ", bg="#B8BBC5")
    unavailable = tk.Label(win1, text="Unavailable Hours: ", bg="#B8BBC5")
    pref_event = tk.Label(win1, text="Preferred Event Type: ", bg="#B8BBC5")
    fields = [name, senior, unavailable, pref_event]

    nrow = 1
    for field in fields: 
        field.grid(row=nrow, column = 0)
        nrow += 1

    # name
    name_field = tk.Entry(win1, width=22)
    name_field.grid(row=1, column=1)

    availability_btn = tk.Button(win1, text="Choose Unavailability")
    availability_btn.config(width=22)
    availability_btn.grid(row=3, column=1)
    availability_btn['command'] = window_calendar

    comboSenior = tk.ttk.Combobox(win1, values=["Y", "N"], width=22)
    comboSenior.grid(row=2, column=1)

    comboEvent = tk.ttk.Combobox(win1, values=["Art", "Music", "Theater", "Reception", "Dance", "No Preference"], width=22)
    comboEvent.grid(row=4, column=1)

    submit = tk.Button(win1, text="Submit") 
    submit.grid(row=5, column=1) 
    submit['command'] = submit_employee(name_field)

    win1.mainloop()
   

def submit_employee(name_field):
    text = name_field.get()
    print(text)

# create calendar window 
def window_calendar():
    win_calendar = tk.Toplevel()
    win_calendar.geometry("625x380+20+20")
    win_calendar["bg"] = "#B8BBC5"
    title = tk.Label(win_calendar, text="Choose Unavailability", bg="#B8BBC5",pady=50)
    title.grid(row = 0, column = 0)
    calendar = Unavailable_hour(win_calendar)
    calendar.grid(row = 1, column = 0)


# available selection window
class Unavailable_hour(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.tree = ttk.Treeview(parent, columns=("size", "modified"))
        self.tree["columns"] = ("Sunday","Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday")

        self.tree.column("Sunday", width=60)
        self.tree.column("Monday", width=60)
        self.tree.column("Tuesday", width=60)
        self.tree.column("Wednesday", width=60)
        self.tree.column("Thursday", width=60)
        self.tree.column("Friday", width=60)
        self.tree.column("Saturday", width=60)

        self.tree.heading("Sunday", text="Sunday")
        self.tree.heading("Monday", text="Monday")
        self.tree.heading("Tuesday", text="Tuesday")
        self.tree.heading("Wednesday", text="Wednesday")
        self.tree.heading("Thursday", text="Thursday")
        self.tree.heading("Friday", text="Friday")
        self.tree.heading("Saturday", text="Saturday")
        self.tree.bind('<ButtonRelease-1>', self.selectItem)
        self.selectedDict = collections.defaultdict(list)

        self.tree.insert("","end",text = "6-8 AM",values = ("  ","  ","  ","  ","  ","  ","  "),tags = ('odd'))
        self.tree.insert("","end",text = "8-10 AM",values = ("  ","  ","  ","  ","  ","  ","  "),tags = ('even'))
        self.tree.insert("","end",text = "10-12 PM",values = ("  ","  ","  ","  ","  ","  ","  "),tags = ('odd'))
        self.tree.insert("","end",text = "12-2 PM",values = ("  ","  ","  ","  ","  ","  ","  "),tags = ('even'))
        self.tree.insert("","end",text = "2-4 PM",values = ("  ","  ","  ","  ","  ","  ","  "),tags = ('odd'))
        self.tree.insert("","end",text = "4-6 PM",values = ("  ","  ","  ","  ","  ","  ","  "),tags = ('even'))
        self.tree.insert("","end",text = "6-8 PM",values = ("  ","  ","  ","  ","  ","  ","  "),tags = ('odd'))
        self.tree.insert("","end",text = "8-10 PM",values = ("  ","  ","  ","  ","  ","  ","  "),tags = ('even'))
        self.tree.insert("","end",text = "10-12 AM",values = ("  ","  ","  ","  ","  ","  ","  "),tags = ('odd'))
        self.tree.insert("","end",text = "12-2 AM",values = ("  ","  ","  ","  ","  ","  ","  "),tags = ('even'))
        self.tree.insert("","end",text = "2-4 AM",values = ("  ","  ","  ","  ","  ","  ","  "),tags = ('odd'))
        self.tree.insert("","end",text = "4-6 AM",values = ("  ","  ","  ","  ","  ","  ","  "),tags = ('even'))
        # self.tree.tag_configure('oddrow', background='steelblue')
        self.tree.tag_configure('even', background='lightsteelblue')
        self.tree.grid()


    def selectItem(self, event):
        curItem = self.tree.item(self.tree.focus())
        col = self.tree.identify_column(event.x)
        print ('curItem = ', curItem)
        print ('col = ', col)

        col_i = int(col[1])-1
        # print("aaaaaaaaaaa", self.tree["columns"][col_i])
        if curItem["text"] not in self.selectedDict[self.tree["columns"][col_i]]:
            self.selectedDict[self.tree["columns"][col_i]].append(curItem["text"])
        else:
            print("slot has already selected")

        if col == '#0':
            cell_value = curItem['text']
        elif col == '#1':
            cell_value = curItem['text'] + " selected"
        elif col == '#2':
            cell_value = curItem['text'] + " selected"
        elif col == '#3':
            cell_value = curItem['text'] + " selected"
        elif col == '#4':
            cell_value = curItem['text'] + " selected"
        elif col == '#5':
            cell_value = curItem['text'] + " selected"
        elif col == '#6':
            cell_value = curItem['text'] + " selected"
        elif col == '#7':
            cell_value = curItem['text'] + " selected"
        print ('cell_value = ', cell_value)
        print(self.selectedDict)

# add_event window 
def window_event():
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

    comboEvent = tk.ttk.Combobox(win2, values=["Day Events", "Night Events", "Over-night Events"],width=22)
    comboEvent.grid(row=1, column=1)
    comboSenior = tk.ttk.Combobox(win2, values=[i/2 for i in range(1,11)],width=22)
    comboSenior.grid(row=2, column=1)
    comboSenior = tk.ttk.Combobox(win2, values=[i for i in range(1,31)],width=22)
    comboSenior.grid(row=3, column=1)

# staff event window
def window_staff():
    win3 = tk.Toplevel(root)
    win3.geometry("920x600+20+20")
    win3["bg"] = "#B8BBC5"
    title = tk.Label(win3, text="Staff an Event", bg="#B8BBC5",pady=50)
    title.pack()

#==========================
#      MAIN INTERFACE
#==========================

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
add_employee_btn['command']=window_employee
add_event_btn['command']=window_event
staff_event_btn['command']=window_staff

root.mainloop()

    