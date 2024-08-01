class Class1(object):
    def name(self):
        name = input("Enter the student's name: ")
        self.name = name

class Class2(Class1):
    def age(self):
        age = int(input("Enter the student's age: "))
        self.age = age

class Class3(Class2):
    def rollno(self):
        rollno = int(input("Enter the roll no. of the student: "))
        self.rollno = rollno

    def show(self):
        print(f"Name of student is {self.name}")
        print(f"Age of student is {self.age}")
        print(f"Roll no. of student is: {self.rollno}")

obj = Class3()

obj.name()
obj.age()
obj.rollno()
print("\n")
obj.show()