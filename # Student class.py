# Student class
class Student:
    def __init__(self, student_id, name, age, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("\nStudent ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)


# Student Management System class
class StudentManagementSystem:
    def __init__(self):
        self.students = []

    # Add multiple students
    def add_students(self):
        n = int(input("How many students do you want to add? "))

        for i in range(n):
            print(f"\nEnter details for student {i + 1}")

            student_id = int(input("Enter Student ID: "))

            # Check for duplicate ID
            for student in self.students:
                if student.student_id == student_id:
                    print("Student ID already exists! Skipping this student.")
                    break
            else:
                name = input("Enter Student Name: ")
                age = int(input("Enter Age: "))
                marks = float(input("Enter Marks: "))

                student = Student(student_id, name, age, marks)
                self.students.append(student)
                print("Student added successfully!")

    # View all students
    def view_students(self):
        if len(self.students) == 0:
            print("No students found!")
        else:
            print("\n----- Student Details -----")
            for student in self.students:
                student.display()

    # Search student by ID
    def search_student(self):
        student_id = int(input("Enter Student ID to search: "))

        for student in self.students:
            if student.student_id == student_id:
                student.display()
                return

        print("No student found!")

    # Update student marks
    def update_marks(self):
        student_id = int(input("Enter Student ID: "))

        for student in self.students:
            if student.student_id == student_id:
                new_marks = float(input("Enter updated marks: "))
                student.marks = new_marks
                print("Marks updated successfully!")
                return

        print("Student not found!")

    # Delete student record
    def delete_student(self):
        student_id = int(input("Enter Student ID to delete: "))

        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student record deleted successfully!")
                return

        print("Student not found!")


# Main Program
sms = StudentManagementSystem()

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Students")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        sms.add_students()
    elif choice == 2:
        sms.view_students()
    elif choice == 3:
        sms.search_student()
    elif choice == 4:
        sms.update_marks()
    elif choice == 5:
        sms.delete_student()
    elif choice == 6:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")