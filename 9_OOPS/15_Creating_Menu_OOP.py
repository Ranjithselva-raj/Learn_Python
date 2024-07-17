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

while True:
    choice = input("Enter your choice: \n1) Add student \n2) Display students \n5) Exit \n")
    if choice == "1":
        #Accepting data from the user to create student object
        name=input("Enter the name of student: ")
        age = int(input("Enter the age of student: "))
        roll_number = int(input("Enter the roll number of student: "))

        #creating student object and adding to school 
        school.add_student(name, age, roll_number)
    
    elif choice == "2":
        if len(school.students) == 0:
            print("No students added yet")
        else:
            #displaying students
            school.display_students()

    elif choice == "5":
        break








