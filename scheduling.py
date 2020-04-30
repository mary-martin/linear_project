from data import *
from __future__ import print_function
import sys
from ortools.constraint_solver import pywrapcp

def schedule_event(event_name):

    solver = pywrapcp.Solver("staffing")
    employees = get_all_employees
    event = data.get_event(event_name)
    num_employees = event.num_employees

    # constraints on hours worked per week < 20

    #