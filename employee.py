"""
Handles employee-related operations including
add, view, update, delete, and logout.
"""

from typing import List, Tuple
from database import get_connection


def add_employee() -> None:
    """
    Add a new employee to the database.
    """
    name = input("Name: ").strip()
    age = int(input("Age: ").strip())
    department = input("Department: ").strip()
    salary = float(input("Salary: ").strip())

    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO employees (name, age, department, salary)
            VALUES (?, ?, ?, ?)
            """,
            (name, age, department, salary),
        )

    print("✅ Employee added successfully")


def view_employees() -> None:
    """
    Display all employees.
    """
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT id, name, age, department, salary FROM employees"
        )
        rows: List[Tuple] = cursor.fetchall()

    if not rows:
        print("❌ No employees found")
        return

    print("\nID | Name | Age | Department | Salary")
    print("-" * 50)
    for row in rows:
        print(row)


def update_employee() -> None:
    """
    Update an employee's salary.
    """
    emp_id = int(input("Enter Employee ID to update: ").strip())
    new_salary = float(input("New Salary: ").strip())

    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE employees SET salary = ? WHERE id = ?",
            (new_salary, emp_id),
        )

    print("✅ Employee updated successfully")


def delete_employee() -> None:
    """
    Delete one or multiple employees using comma-separated IDs.
    """
    ids_input = input(
        "Enter Employee ID(s) to delete (comma separated): "
    ).strip()

    try:
        emp_ids = [int(emp_id.strip()) for emp_id in ids_input.split(",")]
    except ValueError:
        print("❌ Invalid input. Please enter numbers only.")
        return

    placeholders = ",".join("?" for _ in emp_ids)
    query = f"DELETE FROM employees WHERE id IN ({placeholders})"

    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(query, emp_ids)

    print("✅ Employee(s) deleted successfully")


def delete_multiple_employees() -> None:
    """
    Delete multiple employees using comma-separated IDs.
    """
    ids_input = input(
        "Enter employee IDs to delete (comma separated): "
    ).strip()

    emp_ids = [int(emp_id) for emp_id in ids_input.split(",")]

    placeholders = ",".join("?" for _ in emp_ids)

    query = f"DELETE FROM employees WHERE id IN ({placeholders})"

    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(query, emp_ids)

    print("✅ Selected employees deleted successfully")


def logout() -> bool:
    """
    Log out and terminate the program from employee menu.

    Returns:
        bool: False to stop menu loop
    """
    print()
    print("🔒 Logged out successfully")
    return False
