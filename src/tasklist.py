import datetime as dt

from task import Task

class TaskList:
    def __init__(self):
        self.tasks = []
        self.length = 0

    def add_task(self, task):
        #TODO add duplicate checking
        if isinstance(task, Task) == False:
            raise Exception(f"Invalid argument passed. You must pass a Task variable.")
        
        print(f"Adding {task.name} to task list...")
        self.tasks.append(task)
        self.length = len(self.tasks)

    def remove_task(self, task):
        if isinstance(task, Task) == False:
            raise Exception(f"Invalid argument passed. You must pass a Task variable.")

        for item in self.tasks:
            if task.name == item.name:
                print(f"Removing {task.name} from task list...")
                self.tasks.remove(item)
                self.length = len(self.tasks)
                return
        raise Exception(f"{task.name} not found in task list...")

    def show_tasks(self):
        print(f"Displaying {self.length} tasks:")
        for task in self.tasks:
            print("\n----------------------------------------")
            print(f"--> Name: {task.name}")
            print(f"--> Frequency: {task.cycle_duration.days} days") #TODO figure out if I can do this better
            print(f"--> Next Due Date: {task.due}")
            print(f"--> Time til Due Date: {(task.due - dt.date.today()).days} days")
            print("----------------------------------------")

    def generate_file(self):
        file_content = ''
        for task in self.tasks:
            file_content += task.name + ','
            file_content += str(task.cycle_duration.days) + ','
            file_content += str(task.start)
            file_content += '['
        return file_content.rstrip('[')

    def generate_list_from_file(self, file_content):
        text_tasks = file_content.split('[')
        print(text_tasks)
        for tt in text_tasks:
            tt = tt.split(',')
            name = tt[0]
            duration = dt.timedelta(int(tt[1]))
            start = dt.date.fromisoformat(tt[2])
            task = Task(name, duration, start)
            self.add_task(task)