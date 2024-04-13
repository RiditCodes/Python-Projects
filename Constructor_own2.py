class Student:
    def __init__(self, name, age, grade, section):
        self.name = name
        self.age = age
        self.grade = grade
        self.section = section

    def show(self):
        print("\n")
        print("Student name is: ", self.name)
        print("Student age is: ", self.age)
        print("Student grade is: ", self.grade)
        print("Student section is: ", self.section)

name = input("Enter name of student1: ")
age = int(input("Enter age of student1: "))
grade = input("Enter grade of student1: ")
section = input("Enter section of student1: ")

student1 = Student(name, age, grade, section)
print("\n")

name = input("Enter name of student2: ")
age = int(input("Enter age of student2: "))
grade = input("Enter grade of student2: ")
section = input("Enter section of student2: ")

student2 = Student(name, age, grade, section)

student1.show()
student2.show()