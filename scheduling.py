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

    # 2 hr intervals starting at 6 am
    # event intervals
    for event in events:
        

     
    
    # print(event)
    
def set_schedule(employees):
    db.staff_event(employees)
    print(schedule_set)

def show_solutions():
    return 