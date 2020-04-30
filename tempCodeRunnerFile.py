_event():
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

    comboEvent = tk.ttk.Combobox(win2, values=["Art", "Music", "Theater", "Reception", "Dance", "No Preference"],width=22)
    comboEvent.grid(row=1, column=1)
    comboSenior = tk.ttk.Combobox(win2, values=[i/2 for i in range(1,11)],width=22)
    comboSenior.grid(row=2, column=1)
    comboSenior = tk.ttk.Combobox(win2, values=[i for i in range(1,31)],width=22)
    comboSenior