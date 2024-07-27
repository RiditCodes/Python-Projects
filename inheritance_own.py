class Student1(object):
    def __init__(self, marks):
        self.marks = marks

    def display(self):
        print("Student1 class")
        return self.marks

class Student2(Student1):
    None

marks = int(input("Enter marks of Student 1: "))
marks1 = Student1(marks)
marks = int(input("Enter marks of Student 2: "))
marks2 = Student2(marks)

print(marks2.display())
print("Marks of student 1 are: ",marks1.display())