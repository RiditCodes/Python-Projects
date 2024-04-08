class Employee:
    def __init__(self):
        print("Non-parameterized constructor")

    def display(self, name):
        print("Employee name: ", name)

emp = Employee()
text = input("Enter name: ")
emp.display(text)