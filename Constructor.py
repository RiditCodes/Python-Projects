class Employee:
    def __init__(self, name):
        print("Parameterized constructor")
        self.name = name
    def display(self):
        print(f"Employee Name: {self.name}")

text = input("Enter name: ")
employee = Employee(text)
employee.display()