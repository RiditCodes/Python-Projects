class Base(object):
    def getData(self, a):
        self.a = a

class Derived(Base):
    def readData(self, b):
        self.b = b

    def product(self):
        print(self.a*self.b)

Derived_object = Derived()
x = int(input("Enter number: "))
y = int(input("Enter another number: "))
Derived_object.getData(x)
Derived_object.readData(y)
Derived_object.product()