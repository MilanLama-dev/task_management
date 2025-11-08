import filehandler
from utils import input_deadline, options_manager, options_employee

tasks = []

def create_task():
    task_name = input("Enter task name: ").strip()
    if not task_name:
        print("Task name cannot be empty.")
        return

    deadline = input_deadline()
    task = {
        "Task Name": task_name,
        "Status": "pending",
        "Deadline": deadline
    }
    tasks.append(task)
    filehandler.save_tasks_to_file(tasks)
    print("Task created successfully.")

def see_task():
    if not tasks:
        print("No tasks to display.")
        return
    print("\nTasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['Task Name']} — Status: {task['Status']} — Deadline: {task['Deadline']}")

def delete_task():
    see_task()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            filehandler.save_tasks_to_file(tasks)
            print(f"Task '{removed['Task Name']}' deleted successfully.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def modify_task():
    see_task()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to modify: "))
        if 1 <= index <= len(tasks):
            new_name = input("Enter new task name: ").strip()
            if new_name:
                tasks[index - 1]["Task Name"] = new_name
            new_deadline = input_deadline()
            tasks[index - 1]["Deadline"] = new_deadline
            filehandler.save_tasks_to_file(tasks)
            print("Task modified successfully.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def task_status():
    see_task()
    if not tasks:
        return
    try:
        index = int(input("Enter task number to change status: "))
        if 1 <= index <= len(tasks):
            task = tasks[index - 1]
            task["Status"] = "done" if task["Status"] == "pending" else "pending"
            filehandler.save_tasks_to_file(tasks)
            print(f"Task status updated to '{task['Status']}'.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def core_function_manager():
    while True:
        options_manager()
        try:
            choice = int(input("Enter your option: "))
            if choice == 1:
                create_task()
            elif choice == 2:
                see_task()
            elif choice == 3:
                delete_task()
            elif choice == 4:
                modify_task()
            elif choice == 5:
                task_status()
            elif choice == 6:
                print("Goodbye Manager!")
                break
            else:
                print("Invalid input.")
        except ValueError:
            print("Please enter a number.")

def core_function_employee():
    while True:
        options_employee()
        try:
            choice = int(input("Enter your option: "))
            if choice == 1:
                see_task()
            elif choice == 2:
                task_status()
            elif choice == 3:
                print("Goodbye Employee!")
                break
            else:
                print("Invalid input.")
        except ValueError:
            print("Please enter a number.")