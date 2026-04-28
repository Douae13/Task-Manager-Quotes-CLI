import db
from auth import register, login
from tasks import add_task, view_tasks, mark_done, delete_task

def task_menu(user_id):
    while True:
        print("\n===== TASK MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        
        choice = input("> ")

        if choice == "1":
            task = input("Task: ")
            add_task(user_id, task)
        
        elif choice == "2":
            tasks = view_tasks(user_id)
            for t in tasks:
                status = "✔" if t[2] else "✖"
                print(t[0], t[1], status)

        elif choice == "3":
            task_id = input("Task ID: ")
            mark_done(task_id)

        elif choice == "4":
            task_id = input("Task ID: ")
            delete_task(task_id)

def main():
    db.db_init()

    while True:
        print("\n===== MAIN MENU =====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("> ")

        if choice == "1":
            u = input("Username: ")
            p = input("Password: ")
            if register(u, p):
                print("Registered successfully!")
            else:
                print("User exists")

        elif choice == "2":
            u = input("Username: ")
            p = input("Password: ")
            user_id = login(u, p)

            if user_id:
                print("Login Successful!")
                task_menu(user_id)
            else:
                print("Invalid Login")
        
        elif choice == "3":
            break;

main()