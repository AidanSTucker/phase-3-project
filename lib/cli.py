# database/cli.py

from helpers import (
    exit_program,
    create_user,
    delete_user,
    get_all_users,
    find_users_by_department,
    create_task,
    delete_task,
    get_all_tasks,
    find_tasks_by_department,
    find_task_by_id,
    find_user_by_id
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            get_all_tasks()
        elif choice == "2":
            get_all_users()
        elif choice == "3":
            find_tasks_by_department()
        elif choice == "4":
            find_users_by_department()
        elif choice == "5":
            create_task()
        elif choice == "6":
            delete_task()
        elif choice == "7":
            create_user()
        elif choice == "8":
            delete_user()
        elif choice == "9":
            find_task_by_id()
        elif choice == "10":
            find_user_by_id()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. View all tasks")
    print("2. View all users")
    print("3. View tasks by department")
    print("4. View users by department")
    print("5. Add new task")
    print("6. Delete task")
    print("7. Add new user")
    print("8. Delete user")
    print("9. Find task by department")
    print("10. Find user by department")


if __name__ == "__main__":
    main()
