#Hybrid Inheritance

import math

class BaseAndHeight:
    def __init__(self):
        self.base = int(input("Enter length of base of triangle: "))
        self.height = int(input("Enter height of triangle: "))

class Area(BaseAndHeight):
    def AreaofTriangle(self):
        area = (self.base * self.height) / 2
        print(f"Area of triangle is: {area} cm")
    
class Hypotenuse(BaseAndHeight):
    def hypotenuse(self):
        self.hypotenuse = math.sqrt((self.base ** 2) + (self.height ** 2))
        print(f"Hypotenuse of triangle is: {self.hypotenuse} cm")

class Perimeter(Hypotenuse):
    def perimeter(self):
        Hypotenuse.hypotenuse(self)
        perimeter = self.hypotenuse + self.base + self.height
        print(f"Perimeter of triangle is: {perimeter} cm")

area = Area()
perimeter = Perimeter()
print("\n")
area.AreaofTriangle()
perimeter.perimeter()