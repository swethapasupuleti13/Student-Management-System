from student import Student
import filehandler as fh

def get_student_input():
    while True:
        # 1. Validate ID
        sid = input("Enter ID: ").strip()
        if not sid.isdigit():
            print("[!] Error: ID must be a number. Try again.\n")
            continue

        # 2. Validate Name
        name = input("Enter Name: ").strip()
        if not name.replace(" ", "").isalpha() or not name:
            print("[!] Error: Name must contain only letters. Try again.\n")
            continue

        # 3. Validate Age
        age = input("Enter Age: ").strip()
        if not age.isdigit():
            print("[!] Error: Age must be a number (e.g., 20). Try again.\n")
            continue

        # 4. Validate Course
        course = input("Enter Course: ").strip()
        if not course:
            print("[!] Error: Course cannot be empty. Try again.\n")
            continue

        # If all checks pass, create the object
        try:
            return Student(sid, name, age, course)
        except ValueError as e:
            print(f"[!] {e}")
            continue

def menu():
     while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Enter choice: ")

        if choice == "1":
            student_obj = get_student_input()
            fh.add_student(student_obj)
        
        elif choice == "2":
            fh.view_students()
            
        elif choice == "3":
            sid = input("Enter ID to search: ")
            fh.search_student(sid)
            
        elif choice == "4":
            sid = input("Enter ID to update: ")
            print("Enter new details:")
            updated_student = get_student_input()
            # Force the ID to match the one we searched for
            updated_student.student_id = sid 
            fh.update_student(updated_student)
            
        elif choice == "5":
            sid = input("Enter ID to delete: ")
            fh.delete_student(sid)
            
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()
