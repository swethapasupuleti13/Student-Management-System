# Student Management System

A robust, console-based CRUD (Create, Read, Update, Delete) application built with **Python**. This project demonstrates a clean separation of concerns by modularizing the data model, storage logic, and user interface.

## 🚀 Features

* **Full CRUD Functionality:** Add, view, search, update, and delete student records seamlessly.
* **Persistent Storage:** Data is saved to a `students.json` file, ensuring records are maintained across sessions.
* **Input Validation:** * Ensures IDs and Ages are numeric.
    * Validates names to contain only alphabetic characters.
    * Prevents empty fields and duplicate entries.
* **Layered Architecture:** * `student.py`: Object-Oriented model with built-in validation and error handling.
    * `file_handler.py`: Dedicated module for JSON I/O operations.
    * `main.py`: Interactive menu-driven interface.

## 🛠️ Technical Stack

* **Language:** Python 3.13+
* **Data Format:** JSON (JavaScript Object Notation)
* **Key Concepts:** Object-Oriented Programming (OOP), File Handling, Exception Handling.

## 📂 Project Structure

```text
student_management_sys/
│
├── main.py           # Entry point & Menu Interface
├── student.py        # Student Class & Logic Validation
├── file_handler.py   # JSON Read/Write operations
└── students.json     # Local database (auto-generated)
