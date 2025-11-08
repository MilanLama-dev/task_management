from tasks import core_function_manager, core_function_employee

roles = {
    "manager": "Manager123",
    "employee": "employee123"
}

def login():
    print("Which user are you?")
    print("1. Manager")
    print("2. Employee")

    choice = input("Enter your role (manager/employee): ").strip().lower()
    if choice in roles:
        password = input("Enter password: ")
        if password == roles[choice]:
            if choice == "manager":
                core_function_manager()
            else:
                core_function_employee()
        else:
            print("❌ Password is incorrect.")
    else:
        print("❌ Role not found.")