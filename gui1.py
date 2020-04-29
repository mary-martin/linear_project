#!/usr/bin/env python3
import tkinter as tk
import tkinter.ttk
from data import * 

root = tk.Tk()
root.geometry("925x600")

# add_employee window
def window_employee():
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

    tk.Entry(win1, width=22).grid(row=1, column=1)
    tk.Entry(win1, width=22).grid(row=3, column=1)

    comboSenior = tk.ttk.Combobox(win1, values=["Y", "N"], width=22)
    comboSenior.grid(row=2, column=1)
    comboEvent = tk.ttk.Combobox(win1, values=["Day Shifts", "Night Shifts", "Over-night Shifts", "Flexible"], width=22)
    comboEvent.grid(row=4, column=1)

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
