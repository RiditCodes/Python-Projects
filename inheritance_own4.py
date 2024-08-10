#Hierarchical Inheritance

class Person:
    def getData(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))

    def showData(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Teacher(Person):
    def inputData(self):
        Person.getData(self)
        self.school = input("Enter school name: ")
        self.sub = input("Enter subject taught: ")

    def displayData(self):
        Person.showData(self)
        print(f"Name of school: {self.school}")
        print(f"Name of subject taught: {self.sub}")

class Parent(Person):
    def writeData(self):
        Person.getData(self)
        self.child = input("Enter name of child: ")
        self.job = input("Enter name of company: ")

    def outputData(self):
        Person.showData(self)
        print(f"Name of child: {self.child}")
        print(f"Working for: {self.job}")

teacher = Teacher()
parent = Parent()

print("Enter details of the teacher...")
teacher.inputData()
print("\nEnter details of the parent...")
parent.writeData()
print("\nDetails of the teacher...")
teacher.displayData()
print("\nDetails of the parent...")
parent.outputData()