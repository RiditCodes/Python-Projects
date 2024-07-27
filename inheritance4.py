class BaseClass1(object):
    def Area(self, length, breadth):
        return length*breadth

class BaseClass2(object):
    def Perimeter(self, length, breadth):
        return 2*(length+breadth)

class DerivedClass(BaseClass1, BaseClass2):
    def Rectangle_Area(self, length, breadth):
        return BaseClass1.Area(self, length, breadth)
    def Rectangle_Perimeter(self, length, breadth):
        return BaseClass2.Perimeter(self, length, breadth)

length = int(input("Enter length of rectangle: "))
breadth = int(input("Enter breadth of rectangle: "))

obj = DerivedClass()

print("Area of rectangle: ", obj.Rectangle_Area(length, breadth), "sq. cm")
print("Perimeter of rectangle: ", obj.Rectangle_Perimeter(length, breadth), "cm")
