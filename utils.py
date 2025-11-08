import datetime

def options_manager():
    print("\nOptions:")
    print("1. Create task")
    print("2. See tasks")
    print("3. Delete task")
    print("4. Modify task")
    print("5. Change task status")
    print("6. Exit")

def options_employee():
    print("\nOptions:")
    print("1. See tasks")
    print("2. Change task status")
    print("3. Exit")

def input_deadline():
    while True:
        date_input = input("Enter deadline (YYYY-MM-DD): ").strip()
        if not date_input:
            print("⚠️ Deadline cannot be empty.")
            continue
        try:
            datetime.datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("❌ Invalid date format. Please use YYYY-MM-DD.")