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
        duration = int(event['duration']).ceil()
        end_hours = start_hours + duration


     
    
    # print(event)
    
def set_schedule(employees):
    db.staff_event(employees)
    print(schedule_set)

def show_solutions():
    return 