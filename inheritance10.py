#Hybrid Inheritance

class SuperClass1:
    def display(self):
        print("Inside parent class 1")

class SuperClass2:
    def display(self):
        print("Inside parent class 2")

class SubClass1(SuperClass2, SuperClass1):
    def display(self):
        super().display()

class SubClass2(SuperClass1, SuperClass2):
    def display(self):
        super().display()

subclass1 = SubClass1()
subclass2 = SubClass2()

subclass1.display()
subclass2.display()