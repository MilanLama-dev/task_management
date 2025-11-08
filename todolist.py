from auth import login
from filehandler import load_tasks_from_file

def main():
    load_tasks_from_file()
    login()

if __name__ == "__main__":
    main()