#Multilevel Inheritance

class Parent:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

class Child(Parent):
    def __init__(self, name, model):
        self.model = model
        Parent.__init__(self, name)
    def getModel(self):
        return self.model

class GrandChild(Child):
    def  __init__(self, name, model, price):
        Child.__init__(self, name, model)
        self.price = price

    def getPrice(self):
        return self.price

object_gc = GrandChild("Tata", "Tata NEXON XZ 1.2", "Rs. 700000")
print("Name of company:", object_gc.getName())
print("Name of the model:", object_gc.getModel())
print("Price of laptop:", object_gc.getPrice())