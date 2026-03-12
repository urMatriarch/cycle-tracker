import datetime as dt

class Task:
    def __init__(self, name, start = dt.datetime.now(), due = None):
        self.name = name
        self.start = start
        self.due = due
