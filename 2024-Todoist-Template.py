from todoist_api_python.api import TodoistAPI
import requests
from datetime import date
import datetime
import time
import json

today = date.today()

api = TodoistAPI("API KEY HERE")

today = datetime.date.today().day
datetime.datetime.today()
weekday = datetime.datetime.today().weekday()


#Print Date and Day to Check Code
print (today)
if weekday == 0:
    print('Monday')
elif weekday == 1:
    print("Tuesday")
elif weekday == 2:
    print("Wednesday")
elif weekday == 3:
    print("Thursday")
elif weekday == 4:
    print("Friday")
elif weekday == 5:
    print("Saturday")
elif weekday == 6:
    print("Sunday")
else:
    print("No Day Returned")

#Projects
project1 = "PROJECT NUMBER"
project2 = "PROJECT NUMBER"
Project3 = "PROJECT NUMBER"
Project4 = "PROJECT NUMBER"
project5 = "PROJECT NUMBER"


### TASKS ###

## Daily ##
task = api.add_task(content="Do this every day", project_id = project3, labels = ["Daily"], priority = 3, due_string="today")


#Monday
    
if weekday == 0:
        task = api.add_task(content="Hello, It's Monday", project_id = project1, labels = ["Daily"], priority = 4, due_string="today")
        print ('Monday - Complete')
else:
    print ('Today is not Monday')

#Tuesday
if weekday == 1:
    task = api.add_task(content="Hello, It's Tuesday", project_id = project1, labels = ["Daily"], priority = 4, due_string="today")
    print ('Tuesday - Complete')
else:
    print ('Today is not Tuesday')

#Wednesday
if weekday == 2:
        task = api.add_task(content="Hello, It's Wednesday", project_id = project1, labels = ["Daily"], priority = 4, due_string="today")
        print ('Wednesday - Complete')
else:
    print ('Today is not Wednesday')

#Thursday
if weekday == 3:
    task = api.add_task(content="Hello, It's Thursday", project_id = project1, labels = ["Daily"], priority = 4, due_string="today")
    print ('Thursday - Complete')
else:
    print ('Today is not Thursday')

#Friday
if weekday == 4:
        task = api.add_task(content="Hello, It's Friday", project_id = project1, labels = ["Daily"], priority = 4, due_string="today")
        print ('Friday - Complete')
else:
    print ('Today is not Friday')

#Saturday
if weekday == 5:
    task = api.add_task(content="Hello, It's Saturday", project_id = project1, labels = ["Daily"], priority = 4, due_string="today")
    task = api.add_task(content="Do This Thing on Monday", project_id = project2, labels = ["Weekly"], priority = 4, due_string="Monday")

    print ('Saturday - Complete')
else:
    print ('Today is not Saturday')

#Sunday
if weekday == 6:
        task = api.add_task(content="Hello, It's Sunday", project_id = project1, labels = ["Daily"], priority = 4, due_string="today")
        print ('Sunday - Complete')
else:
    print ('Today is not Sunday')

#1st of Month
if today == 28:
    print('hello')
    task = api.add_task(content="Hello, Do this thing on the first of the month", project_id = project2, labels = ["Daily"], priority = 4, due_string="1st of next month")
    print ('First of Month Tasks Added')
else:
    print('Not the 28th')

