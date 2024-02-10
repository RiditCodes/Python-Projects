class SuperClass1:
    def show(self):
        print("Inside Parent Class 1")

class SuperClass2:
    def show(self):
        print("Inside Parent Class 2")

class SubClass1(SuperClass2, SuperClass1):
    def show(self):
        super().show()

class SubClass2(SuperClass1, SuperClass2):
    def display(self):
        super().show()

sub1 = SubClass1()
sub2 = SubClass2()
sub1.show()
sub2.display()