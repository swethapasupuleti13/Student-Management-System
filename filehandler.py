import json
import os

FILE_NAME = "students.json"

def read_data():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def write_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def add_student(student_obj):
    data = read_data()
    # Check for duplicate ID
    if any(s['id'] == student_obj.student_id for s in data):
        print(f"Error: Student with ID {student_obj.student_id} already exists.")
        return False
    
    data.append(student_obj.to_dict())
    write_data(data)
    print("Student added successfully!")
    return True

def view_students():
    data = read_data()
    if not data:
        print("No student records found.")
        return
    
    print("\n--- Current Student Records ---")
    for s in data:
        print(f"ID: {s['id']}, Name: {s['name']}, Age: {s['age']}, Course: {s['course']}")
