"""
Handles database connection and table creation for the EMS project.
"""

import sqlite3
from sqlite3 import Connection

DATABASE_NAME = "ems.db"


def get_connection() -> Connection:
    """
    Create and return a connection to the SQLite database.

    Returns:
        sqlite3.Connection: SQLite database connection object
    """
    return sqlite3.connect(DATABASE_NAME)


def create_tables() -> None:
    """
    Create required tables (users, employees) if they don't exist.
    """
    with get_connection() as connection:
        cursor = connection.cursor()

        # Users table with password as BLOB to store bcrypt hash
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password BLOB NOT NULL
            )
            """
        )

        # Employees table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                department TEXT NOT NULL,
                salary REAL NOT NULL
            )
            """
        )


# Create tables automatically if running this module
if __name__ == "__main__":
    create_tables()
    print("✅ Database tables created successfully")
