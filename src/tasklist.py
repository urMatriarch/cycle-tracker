from task import Task

class TaskList:
    def __init__(self):
        self.tasks = []
        self.length = 0

    def add_task(self, task):
        if isinstance(task, Task) == False:
            raise Exception(f"Invalid argument passed. You must pass a Task variable.")
        
        print(f"Adding {task.name} to task list...")
        self.tasks.append(task)
        self.length = len(self.tasks)

    def remove_task(self, task):
        if isinstance(task, Task) == False:
            raise Exception(f"Invalid argument passed. You must pass a Task variable.")

        for item in self.tasks:
            if task == item:
                print(f"Removing {task.name} from task list...")
                self.tasks.remove(item)
                self.length = len(self.tasks)
                return
        raise Exception(f"{task.name} not found in task list...")