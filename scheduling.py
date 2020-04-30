from data import *
from ortools.sat.python import cp_model

def schedule_event(event_name):

    employees = get_all_employees
    event = data.get_event(event_name)

    # constraints on hours worked per week < 20

    #