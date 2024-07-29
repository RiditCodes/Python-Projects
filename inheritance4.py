#Multiple Inheritance

class BaseClass1(object):
    def Area(self, length, breadth):
        return length*breadth

class BaseClass2(object):
    def Perimeter(self, length, breadth):
        return 2*(length+breadth)

class DerivedClass(BaseClass1, BaseClass2):
    def Area_Rectangle(self, l, b):
        return BaseClass1.Area(self, l, b)
    
    def Perimeter_Rectangle(self, length, breadth):
        return BaseClass2.Perimeter(self, length, breadth)

Derived_object = DerivedClass()
l = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))

print("Area of rectangle: ", Derived_object.Area_Rectangle(l, b), "sq. cm")
print("Perimeter of rectangle: ", Derived_object.Perimeter_Rectangle(l, b), "cm")