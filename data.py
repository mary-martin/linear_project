#!/usr/bin/env python3
from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb+srv://mary_martin:If6was9then%3F@lp-cluster-jdvpa.mongodb.net/?authSource=admin")
db = client.admin

# server status command and results 
serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)

def add_event(name, date, time, duration, evt_type, num_employees):
    db=client.event 
    event = {
        'event_name': name,
        'date': date,
        'time': time,
        'duration': duration,
        'type': evt_type, 
        'num_employees': num_employees
    }
    result = db.events.insert_one(event)
    print('event created: ', name)

def add_employee(name, hire_date, can_manage, event_pref, unavailable_hrs):
    db=client.employee
    employee = {
        'name': name,
        'hire_date': hire_date,
        'can_manage': can_manage,
        'event_pref': event_pref,
        'unavailable_hrs': unavailable_hrs
    }
    result = db.employees.insert_one(employee)
    print('employee added: ', name)

def change_event_pref(name, pref):
    employee = db.employees.find_one({'name': name})
    # db.employees.update_one({'_id': { eq: employee.get('_id') } }, { set: { 'event_pref': pref } })
    db.employees.update_one({'_id': employee.get('_id') }, { set: { 'event_pref': pref } })

def get_employee_list():
    db=client.employee
    employee_list = list(db.collection.find({}))
    print("Employee list: ", employee_list)

def get_event_list():
    db=client.event
    event_list = list(db.collection.find({}))
    print("Event list: ", event_list)

def get_employee_count():
    db=client.employee
    employee_count = len(list(db.collection.find({})))
    print("Employee count: ", employee_count)
    return employee_count
