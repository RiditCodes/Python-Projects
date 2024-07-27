class Employee1(object):
    def getdata(self):
        self.emp_name = input("Enter name of the employee: ")
        self.gender = input("Enter gender: ")
        self.age = input("Enter age: ")

    def display(self):
        print("Name:", self.emp_name)
        print("Gender:", self.gender)
        print("Age:", self.age)

class Employee2(Employee1):
    def readdata(self):
        self.company_name = input("Enter name of the company: ")
        self.salary = input("Enter salary of employee: ")

    def show(self):
        print("Company name:", self.company_name)
        print("Salary:", self.salary)

class Employee3(Employee2):
    def inputdata(self):
        self.language_num = input("Enter no. of languages known: ")

    def output(self):
        print("Number of languages known:", self.language_num)

emp3 = Employee3()
emp3.getdata()
emp3.readdata()
emp3.inputdata()
print("\n")
emp3.display()
emp3.show()
emp3.output()