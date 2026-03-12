import datetime as dt

class Task:
    def __init__(self, name, start = dt.datetime.now(), due = None):
        self.name = name
        self.start = start
        self.due = due
        self.is_due = False

    def check_if_due(self):
        if dt.datetime.now() >= self.due:
            print(f"It is {dt.datetime.now()}!")
            print(f"{self.name} is due now!")
            self.is_due = True
        else:
            self.is_due = False
