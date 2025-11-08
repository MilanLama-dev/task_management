import os


TASK_FILE = "data/task.txt"

def save_tasks_to_file(tasks_list):
    if not os.path.exists("data"):
        os.makedirs("data")
    with open(TASK_FILE, "w") as file:
        for task in tasks_list:
            line = f"{task['Task Name']}|{task['Status']}|{task['Deadline']}\n"
            file.write(line)
    print("Tasks saved locally.")

def load_tasks_from_file(tasks_list):
    tasks_list.clear()
    try:
        with open(TASK_FILE, "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    name, status, deadline = parts
                elif len(parts) == 2:
                    name, status = parts
                    deadline = "No deadline set"
                else:
                    continue
                tasks_list.append({
                    "Task Name": name,
                    "Status": status,
                    "Deadline": deadline
                })
        print("Tasks loaded from local file.")
    except FileNotFoundError:
        print("No saved tasks found — starting fresh.")