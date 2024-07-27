class Parent1(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Parent2(object):
    def division(self):
        self.div = self.a / self.b

    def floor_division(self):
        self.floor_div = self.a // self.b

class child(Parent1, Parent2):
    def show(self):
        print(self.a, "/", self.b, "=", self.div)
        print(self.a, "//", self.b, "=", self.floor_div)

a = int(input("Enter number to be divided: "))
b = int(input("Enter number to be divided by: "))
obj_child = child(a, b)
obj_child.division()
obj_child.floor_division()
obj_child.show()