"""
Entry point for the Employee Management System (EMS).
Handles registration, login, employee menu, logout, and exit.
"""

from auth import register, login, logout
from employee import add_employee, view_employees, update_employee, delete_employee


def employee_menu() -> None:
    """
    Display employee management menu after login.
    """
    running = True
    while running:
        print(
            """
Employee Management Menu:
1. Add Employee
2. View Employees
3. Update Employee
4. Delete Employee
5. Logout
"""
        )
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            running = logout()
        else:
            print("❌ Invalid choice. Please try again.")


def main() -> None:
    """
    Main program loop for user registration, login, and exit.
    """
    while True:
        print(
            """
Welcome to Employee Management System (EMS):
1. Register
2. Login
3. Exit
"""
        )
        choice = input("Choose an option: ").strip()

        if choice == "1":
            register()
        elif choice == "2":
            if login():
                employee_menu()
        elif choice == "3":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.")


if __name__ == "__main__":
    main()
