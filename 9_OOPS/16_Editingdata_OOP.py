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

    def edit_student(self, roll_number, new_name, new_age):
        for student in self.students:
            if student.roll_number != roll_number:
                print(f"Student with roll number {roll_number} not found")
            else:
                student.name = new_name
                student.age = new_age
                print(f"Student {student.name} data updated successfully")
                return
            
    def delete_student(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                self.students.remove(student)
                print(f"Student {student.name} deleted successfully")
                return

#creating school object
school = School()

while True:
    choice = input("Enter your choice: \n1) Add student \n2) Display students \n3) Edit student data \n4) Delete student data \n5) Exit \n")
    if choice == "1":
        #Accepting data from the user to create student object
        name=input("Enter the name of student: ")
        age = input("Enter the age of student: ")
        roll_number = input("Enter the roll number of student: ")

        #creating student object and adding to school 
        school.add_student(name, age, roll_number)
    
    elif choice == "2":
        if len(school.students) == 0:
            print("No students added yet")
        else:
            #displaying students
            school.display_students()
    
    elif choice == "3":
        #edit student
        roll_number = input("Enter the roll number of student to edit: ")
        new_name = input("Enter the new name for the student: ")
        new_age = input("Enter the new age for the student: ")

        school.edit_student(roll_number, new_name, new_age)

    elif choice == "4":
        #delete student
        roll_number = input("Enter the roll number of student to delete: ")

        school.delete_student(roll_number)
        
        
    elif choice == "5":
        break
