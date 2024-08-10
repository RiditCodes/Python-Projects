#Hybrid Inheritance

class Person:
    def accept_person_details(self):
        self.id = input("Enter ID: ")
        self.name = input("Enter name: ")

    def display_person_details(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")

class Teaching(Person):
    def accept_teacher_details(self):
        Person.accept_person_details(self)
        self.subject_name = input("Enter name of the subject: ")
        self.teacher_name = input("Enter name of the teacher: ")

    def display_teacher_details(self):
        Person.display_person_details(self)
        print(f"Subject: {self.subject_name}")
        print(f"Teacher: {self.teacher_name}")

class NonTeaching:
    def accept_nonteaching_details(self):
        self.dept_name = input("Enter name of the department: ")

    def display_nonteaching_details(self):
        print(f"Department: {self.dept_name}")

class Instructor(Teaching, NonTeaching):
    def accept_instructor_details(self):
        Teaching.accept_teacher_details(self)
        NonTeaching.accept_nonteaching_details(self)

    def display_instructor_details(self):
        Teaching.display_teacher_details(self)
        NonTeaching.display_nonteaching_details(self)

instructor = Instructor()
print("Enter instructor details...")
instructor.accept_instructor_details()
print("\nInstructor details are given below...")
instructor.display_instructor_details()