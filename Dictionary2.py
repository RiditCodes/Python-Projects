student = {}

print(student)

student["Name"] = input("Enter Name of Student: ")
student["Age"] = int(input("Enter Age of Student: "))
student["Roll no."] = int(input("Enter Roll no. of Student: "))
student["Grade"] = int(input("Enter Grade of Student: "))

print(student)

del student["Roll no."]

print(student)