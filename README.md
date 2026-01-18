# Employee Management System (EMS)

This project demonstrates backend development fundamentals, secure user authentication, and database management using Python and SQLite.

---

## 🚀 Features

- 🔐 Secure user registration and login using **bcrypt password hashing**
- 👤 User authentication system (Register / Login / Logout)
- ➕ Add new employees
- 📋 View all employee records
- ✏️ Update employee salary details
- 🗑️ Delete single or multiple employee records
- 💾 Persistent data storage using **SQLite**
- 🧱 Modular and clean code structure

---

## 🛠️ Technologies Used

- **Python 3**
- **SQLite3**
- **bcrypt** (for password hashing)
- **Object-Oriented & Modular Programming**

---

## 📂 Project Structure

Employee_Management_System/
│
├── .gitignore
├── main.py # Entry point of the application
├── auth.py # User authentication logic
├── employee.py # Employee CRUD operations
├── database.py # Database connection and table creation
├── view.data.py # Utility to view raw employee data
├── ems.db # SQLite database file
└── README.md


---

## ⚙️ How It Works

1. **User Registration**
   - New users register with a username and password.
   - Passwords are securely hashed using bcrypt before storing in the database.

2. **User Login**
   - Registered users log in with valid credentials.
   - Authentication is validated using bcrypt hash comparison.

3. **Employee Management**
   - After login, users can:
     - Add employee details (name, age, department, salary)
     - View all employees
     - Update employee salary
     - Delete one or multiple employees

4. **Logout & Exit**
   - Users can log out securely or exit the application.

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Employee_Management_System.git
cd Employee_Management_System

---

📄 License
This project is licensed under the MIT License.

---


