import data as db
import sys
from ortools.constraint_solver import pywrapcp

def schedule_event():

    solver = pywrapcp.Solver("staffing")
    employees = db.get_employee_list()
    # num_employees = event.num_employees

    # constraints on hours worked per week < 20
    print(employees)
    # print(event)
    
schedule_event()