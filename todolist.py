from auth import login
from Tasks import tasks
from filehandler import load_tasks_from_file

def main():
    load_tasks_from_file(tasks)
    login()

if __name__ == "__main__":
    main()