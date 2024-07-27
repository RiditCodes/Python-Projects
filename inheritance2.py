class Employee(object):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(self.name, self.salary)

class Details(Employee):
    def __init__(self, name, address, salary, department):
        Employee.__init__(self, name, salary)

obj = Details("Ridit", "Haryana", 10000, "Accounts")
obj.show()