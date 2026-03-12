from createtask import create_task

def main():
    test_task = create_task()
    if test_task != None:
        print(f"{test_task.name}")
        print(f"{test_task.start}")
        print(f"{test_task.due}")
    else:
        print("OPE!")


if __name__ == "__main__":
    main()
