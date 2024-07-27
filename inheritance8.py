class Person:
    def getPersonData(self):
        self.id = input("Enter ID: ")
        self.name = input("Enter name: ")

    def display_person(self):
        print("ID:", self.id)
        print("Name:", self.name)

class Teaching(Person):
    def getTeacherData(self):
        Person.getPersonData(self)
        self.subject = input("Enter name of subject: ")
        self.teacher_name = input("Enter name of the teacher: ")

    def display_teacher(self):
        Person.display_person(self)
        print("Subject:", self.subject)
        print("Teacher name:", self.teacher_name)

class NonTeaching:
    def getNonTeachingData(self):
        self.department_name = input("Enter name of the department: ")

    def display_nonteaching(self):
        print("Department:", self.department_name)

class Instructor(Teaching, NonTeaching):
    def getInstructorData(self):
        Teaching.getTeacherData(self)
        NonTeaching.getNonTeachingData(self)

    def display_instructor(self):
        Teaching.display_teacher(self)
        NonTeaching.display_nonteaching(self)

instructor = Instructor()
print("Enter student details...")
instructor.getInstructorData()
print("\nStudent Details are given below...")
instructor.display_instructor()