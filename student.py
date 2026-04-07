class Student:
    """Represents a student record with basic validation."""
    
    def __init__(self, student_id, name, age, course):
        # Strip whitespace and assign
        self.student_id = str(student_id).strip()
        self.name = str(name).strip()
        self.age = int(age)
        self.course = str(course).strip()

        # Final Validation Check
        if not self.student_id.isdigit():
            raise ValueError("ID must be numeric.")
        if not self.name.replace(" ", "").isalpha():
            raise ValueError("Name must contain only letters.")
        if self.age < 0 or self.age > 120:
            raise ValueError("Please enter a valid age.")

    def to_dict(self):
        """Converts object to dictionary for JSON storage."""
        return {
            "id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course
        }

    def __str__(self):
        """Returns a user-friendly string representation."""
        return f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | Course: {self.course}"
