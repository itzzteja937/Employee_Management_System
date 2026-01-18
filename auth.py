"""
Handles user authentication using bcrypt hashing for secure passwords,
registration, login, and logout.
"""

from typing import Optional
import bcrypt
from database import get_connection


def hash_password(password: str) -> bytes:
    """
    Hash a plain-text password using bcrypt.

    Args:
        password (str): User password

    Returns:
        bytes: Hashed password (including salt)
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def register() -> None:
    """
    Register a new user by storing username and hashed password.
    """
    username = input("Enter new username: ").strip()
    password = input("Enter new password: ").strip()

    hashed_password = hash_password(password)

    try:
        with get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed_password),
            )
            print("✅ User registered successfully")

    except Exception:  # pylint: disable=broad-except
        print("❌ Username already exists")


def login() -> bool:
    """
    Validate user login credentials using bcrypt.

    Returns:
        bool: True if login successful, False otherwise
    """
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
        row: Optional[tuple] = cursor.fetchone()

    if row and bcrypt.checkpw(password.encode("utf-8"), row[0]):
        print("✅ Login successful")
        return True

    print("❌ Invalid credentials")
    return False


def logout() -> bool:
    """
    Log out the current user and terminate the program.

    Returns:
        bool: False to stop program loops
    """
    print()
    print("🔒 Logged out successfully")
    # print("👋 Program terminated successfully")
    return False
