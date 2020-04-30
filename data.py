#!/usr/bin/env python3
from pymongo import MongoClient
from pprint import pprint
import datetime

client = MongoClient("mongodb+srv://mary_martin:If6was9then%3F@lp-cluster-jdvpa.mongodb.net/?authSource=admin")
db = client.Staffing

# server status command and results 
serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)

def add_event(name, date, time, duration, evt_type, num_employees):
     
    event = {
        'event_name': name,
        'date': date,
        'time': time, 
        'duration': duration,
        'type': evt_type, 
        'num_employees': num_employees
    }
    result = db.Events.insert_one(event)
    print('event created: ', name)

def add_employee(name, can_manage, event_pref):
    
    if(can_manage == 'N'):
        can_manage = False
    else:
        can_manage = True

    employee = {
        'name': name,
        'can_manage': can_manage,
        'event_pref': event_pref,
        'available_hrs_id': "",
    }
    result = db.Employees.insert_one(employee)
    print('employee added: ', name)

def set_availability(hrs, name):
    
    # fix this, rough draft 
    employee = db.Employees.find_one({'name': name})
    availability = hrs
    # update for each day of the week 
    db.Available_hours.insert_one({'available_hrs': hrs, 'employee_id': employee.get('_id')})

def change_event_pref(name, pref):

    employee = db.Employees.find_one({'name': name})
    db.employees.update_one({'_id': { eq: employee.get('_id') } }, { set: { 'event_pref': pref } })

def get_event(event_name):

    event = db.Events.find_one({'event_name': event_name})
    return event

def set_employee_hrs(hours):

    db.employees.update_one({'_id': employee.get('_id') }, { set: { 'event_pref': pref } })

def get_employee_list():
    
    employee_list = list(db.Employees.find({}))
    print("Employee list: ", employee_list)
    return employee_list

def get_event_list():
    
    event_list = list(db.Events.find({}))
    print("Event list: ", event_list)
    return event_list

def get_employee_count():
   
    employee_count = len(list(db.Events.find({})))
    print("Employee count: ", employee_count)
    return employee_count
