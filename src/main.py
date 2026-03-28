from mainmenu import main_menu
from tasklist import TaskList
from user_createtask import create_task
from user_removetask import user_remove_task
from programstate import Program_State

def main():
    program_state = Program_State()
    program_state.main_menu = True

    task_list = TaskList()
    
    while(program_state.quitting == False):
        if (program_state.main_menu == True):
            main_menu(program_state)
        elif program_state.showing_tasks == True:
            task_list.show_tasks()
            program_state.showing_tasks = False
            program_state.main_menu = True
        elif program_state.adding_task == True:
            task_list.add_task(create_task())
            program_state.adding_task = False
            program_state.main_menu = True
        elif program_state.removing_task == True:
            task_list.remove_task(user_remove_task())
            program_state.removing_task = False
            program_state.main_menu = True

if __name__ == "__main__":
    main()
