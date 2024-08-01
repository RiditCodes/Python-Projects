#Multiple Inheritance

class ParentClass1(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

class ParentClass2(object):
    def check(self):
        if self.age >= 18:
            return 1
        else:
            return 2
        
class ChildClass(ParentClass1, ParentClass2):
    def show(self):
        if ParentClass2.check(self) == 1:
            print(f"{self.name} is eligible for voting. ")
        else:
            print(f"{self.name} is not eligible for voting. ")

name = input("Enter your name: ")
age = int(input("Enter your age: "))

obj = ChildClass(name, age)
obj.show()