from confirmation import confirmation
from task import Task

def user_remove_task():
    valid_input = False
    while valid_input == False:
        print("Please input the name of the task you would like to remove: ")
        name = input("--> ")
        valid_input = confirmation(name, 3, "Remove task with name: ")
    return Task(name)