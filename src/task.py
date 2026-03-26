import datetime as dt

#Task class will hold data for each task to be tracked by the app
#Each class has a name that will display the name of the task - e.g. "Polish Boots"
#It also contains a start date, a duration, and a due date
#Lastly, it has a boolean value showing if it is due or not
class Task:
    def __init__(self, name, duration = dt.timedelta(7), start = dt.date.today()):
        self.name = name
        self.start = start
        self.cycle_duration = duration
        self.due = self.start + self.cycle_duration
        self.is_due = False

    def check_if_due(self):
        if dt.datetime.now() >= self.due:
            print(f"It is {dt.datetime.now()}!")
            print(f"{self.name} is due now!")
            self.is_due = True
        else:
            self.is_due = False
