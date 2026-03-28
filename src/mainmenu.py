from programstate import Program_State

def main_menu(state):
    valid_input = False

    print("What would you like to do?")
    print(f"[S]how tasks  |  [A]dd task  |  [R]emove task  |  [Q]uit")
    choice = input("--> ").lower()
    match (choice):
        case "s" | "show" | "show tasks":
            print("User selected Show Tasks")
            state.main_menu = False
            state.showing_tasks = True
        case "a" | "add" | "add task":
            print("User selected Add Task")
            state.main_menu = False
            state.adding_task = True
        case "r" | "remove" | "remove task":
            print("User selected Remove Task")
            state.main_menu = False
            state.removing_task = True
        case "q" | "quit":
            print("Quitting...")
            state.main_menu = False
            state.quitting = True
            #TODO once file management is set up - this command should save the task list
        case default:
            print("Invalid selection detected. Please try again.")
            state.main_menu = True