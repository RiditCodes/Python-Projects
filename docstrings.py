class Person:
    "This program defines Docstring"

    age = 10

    def function(self):
        print("DOCSTRING")

print(Person.age)

object1 = Person()
print(object1.function())

#docstring can be accessed using the __doc__ method

print(Person.__doc__)