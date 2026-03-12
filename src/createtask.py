from task import Task
from createdate import create_deltatime
import datetime as dt
from confirmation import confirmation

#This function is a dialogue tree to create a task that the user will track
#TODO Reimpliment again with GUI
def create_task():
    valid_input = False
    while valid_input == False:
        print("Please input the name of the task: ")
        name = input("--> ")
        valid_input = confirmation(name, 3, "Create task with name: ")
        duration = create_deltatime()
    return Task(name, duration= duration)
    