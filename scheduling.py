import data as db
import sys
from ortools.sat.python import cp_model


def schedule_week(week_of):

    # set solver to CP Solver
    model = cp_model.CpModel()

    # get specified events
    events = db.get_weekly_events(week_of)
    employees = db.get_employee_list()
    num_employees = event['num_employees']

    week = [False] * 12 * 7
    print(week)

    # 2 hr intervals starting at 6 am
    # event intervals
    for event in events:
        time = event['time']
        start_hours = int(time[0:2])
        start_mins = int(time[3:6])
        print("hours: ", start_hours)
        print("mins: ", start_mins)
        duration = int(event['duration']).ceil()
        print("duration: " + duration)
        end_hours = start_hours + duration
        print(end_hours)


     
    
    # print(event)
    
def set_schedule(employees):
    db.staff_event(employees)

def show_solutions():
    return 