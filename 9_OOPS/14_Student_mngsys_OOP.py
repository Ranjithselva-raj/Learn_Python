class Student:
    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number

class School:
    def __init__(self):
        self.students = []
    
    def add_student(self, name, age, roll_number):
        student = Student(name, age, roll_number)
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            print(f"Name:{student.name},age:{student.age},roll_number:{student.roll_number}")

#creating school object
school = School()

#Accepting data from the user to create student object

name=input("Enter the name of student: ")
age = int(input("Enter the age of student: "))
roll_number = int(input("Enter the roll number of student: "))

#creating student object and adding to school 
school.add_student(name, age, roll_number)

#displaying students
school.display_students()