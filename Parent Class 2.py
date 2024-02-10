class Employee(object):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(self.name)
        print(self.salary)

class Details(Employee):
    def __init__(self, name, salary, address, department):
        super().__init__(name, salary)
        print(address)
        print(department)

obj = Details("Ridit", "Rs. 15,000", "Haryana", "IT Department")
obj.show()