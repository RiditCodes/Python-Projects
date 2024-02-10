import sys
import time

Employee1 = {"Name": "Amit", "Age": 25, "Salary": 5000, "Workstation": "29"}

print(type(Employee1))
print("Accessing employee information....")
time.sleep(1)
print("Error, Session not authorized")
time.sleep(1)
password = 1290
user_password = int(input("Enter password: "))
if user_password == password:
    print("Authorized session, printing employee data in read mode....")
    time.sleep(1)
    print("Name = %s"%Employee1["Name"])
    time.sleep(1)
    print("Age = %d"%Employee1["Age"])
    time.sleep(1)
    print("Salary = %d"%Employee1["Salary"])
    time.sleep(1)
    print("Workstation = %s"%Employee1["Workstation"])
else:
    print("Unauthorized Access!, Blocking session...")
    time.sleep(3)
    sys.exit()