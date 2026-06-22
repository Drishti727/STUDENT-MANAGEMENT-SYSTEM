class Student:  
    def __init__(self , student_id , name , age  , marks): 
        self.student_id = student_id
        self.name = name 
        self.age = age
        self.marks = marks 

    def display(self):
        print("Student_id : self.student_id")
        print("Name : self.name")
        print("Age : self.age")
        print("Marks : self.marks ")

class StudentManagementSystem:
    def __init__(self):
        self.students = []

#add multiple students

    def add_students(self):
        n = int(input("how many students you want to add ?"))  
        for student in self.students:
            if student.student_id == student_id:
                print("Student ID already exists!")
                return

        name = input("Enter Student Name: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))

        student = student(student_id, name, age, marks)
        self.students.append(student)
        print("Student added successfully!")


#view students
def view_students(self):
    if len(self.students) == 0:
        print("no students found !!")
    else:
        print("\n----student Details-----")
    for student in self.student:
        student.display()

#searching student
def search_students(self):
    student_id = int(input("enter student id to search"))
    for student in self.students:
        if student.student_id == student_id:
            student.display()
            return
        print("no student found !! ")

#marks update 
def update_marks(self):
    student_id() = int(input("enter student id"))

    new_marks = float(input("Enter your updated marks "))
    student_marks = new_marks

#delete data
def delete_user(self):
    student_id = int(input("enter your id"))
    
    for student in self.students:
        if student.student_id == student_id:
            self.student.remove(student)

            print("student data deleted !!! ")

sms = StudentManagementSystem
while True:
    print("\n=====STUDENT MANAGEMENT STYSTEM======")
    print()
