from task import Task

def main():
    test_task = Task("Polish boots")
    print(test_task.name)
    print(test_task.start.ctime())


if __name__ == "__main__":
    main()
