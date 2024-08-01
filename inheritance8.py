#Hierarchical Inheritance

class Person:
    def getData(self):
        self.name = input("Enter name: ")
        self.gender = input("Enter gender: ")
        self.age = input("Enter age: ")

    def display(self):
        print("Name: ", self.name)
        print("Gender: ", self.gender)
        print("Age: ", self.age)

class Student(Person):
    def readData(self):
        self.institute = input("Enter name of the school: ")
        self.grade = input("Enter class: ")

    def show(self):
        print("School: ", self.institute)
        print("Grade:", self.grade)

class Employee(Person):
    def inputData(self):
        self.company = input("Enter name of the company: ")
        self.salary = input("Enter salary: Rs.")

    def output(self):
        print("Company: ", self.company)
        print("Salary: ", self.salary)

obj_Student = Student()
obj_Employee = Employee()
print("Enter details of the student...")
obj_Student.getData()
obj_Student.readData()
print("\nEnter details of the employee...")
obj_Employee.getData()
obj_Employee.inputData()
print("\nStudent details are given below...")
obj_Student.display()
obj_Student.show()
print("\nEmployee details are given below...")
obj_Employee.display()
obj_Employee.output()