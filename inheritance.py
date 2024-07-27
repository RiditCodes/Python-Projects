class Employee1(object):
    def __init__(self, name):
        self.name = name

    def display(self):
        print("class Employee1")
        return self.name
    
class Employee2(Employee1):
    def display(self):
        print("class Employee2")
        print(self.name)

emp_name = input("Enter name of the employee: ")
emp1 = Employee1(emp_name)
emp_name = input("Enter name of the employee: ")
emp2 = Employee2(emp_name)

emp2.display()
print(emp1.display())