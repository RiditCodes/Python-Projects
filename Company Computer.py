import sys
import time
import random


Employee1 = {"Name":"Subhash Uppal", "Age":f"{random.randrange(20, 60)}", "Salary per month":"₹23,543", "Job":"IT Department"}
Employee2 = {"Name":"Aamani Tara", "Age":"19", "Salary per month":"₹436", "Job":"Paid Internship"}
Employee3 = {"Name":"Yash Mehrotra", "Age":f"{random.randrange(40, 60)}", "Salary per month":"₹983,641", "Job":"CEO"}
Employee4 = {"Name":"Thomas Addams", "Age":f"{random.randrange(20, 40)}", "Salary per month":"N/A", "Job":"Foreign Client"}
Employee5 = {"Name":"Advit Agarwal", "Age":f"{random.randrange(30, 50)}", "Salary per month":"₹5,509", "Job":"IT Department"}
Employee6 = {"Name":"Yamuna Tikal", "Age":f"{random.randrange(20, 40)}", "Salary per month":"₹12,000", "Job":"Support Team"}

def Authorized(E):
    if E == 1:
        print("Authorized session, printing employee data in read mode....")
        time.sleep(1)
        print("Name = %s"%Employee1["Name"])
        time.sleep(1)
        print("Age = %s"%Employee1["Age"])
        time.sleep(1)
        print("Salary per month = %s"%Employee1["Salary per month"])
        time.sleep(1)
        print("Job = %s"%Employee1["Job"])
    if E == 2:
        print("Authorized session, printing employee data in read mode....")
        time.sleep(1)
        print("Name = %s"%Employee2["Name"])
        time.sleep(1)
        print("Age = %s"%Employee2["Age"])
        time.sleep(1)
        print("Salary per month = %s"%Employee2["Salary per month"])
        time.sleep(1)
        print("Job = %s"%Employee2["Job"])
    if E == 3:
        print("Authorized session, printing employee data in read mode....")
        time.sleep(1)
        print("Name = %s"%Employee3["Name"])
        time.sleep(1)
        print("Age = %s"%Employee3["Age"])
        time.sleep(1)
        print("Salary per month = %s"%Employee3["Salary per month"])
        time.sleep(1)
        print("Job = %s"%Employee3["Job"])
    if E == 4:
        print("Authorized session, printing employee data in read mode....")
        time.sleep(1)
        print("Name = %s"%Employee4["Name"])
        time.sleep(1)
        print("Age = %s"%Employee4["Age"])
        time.sleep(1)
        print("Salary per month = %s"%Employee4["Salary per month"])
        time.sleep(1)
        print("Job = %s"%Employee4["Job"])
    if E == 5:
        print("Authorized session, printing employee data in read mode....")
        time.sleep(1)
        print("Name = %s"%Employee5["Name"])
        time.sleep(1)
        print("Age = %s"%Employee5["Age"])
        time.sleep(1)
        print("Salary per month = %s"%Employee5["Salary per month"])
        time.sleep(1)
        print("Job = %s"%Employee5["Job"])
    if E == 6:
        print("Authorized session, printing employee data in read mode....")
        time.sleep(1)
        print("Name = %s"%Employee6["Name"])
        time.sleep(1)
        print("Age = %s"%Employee6["Age"])
        time.sleep(1)
        print("Salary per month = %s"%Employee6["Salary per month"])
        time.sleep(1)
        print("Job = %s"%Employee6["Job"])

print("Accessing server for employee information....")
time.sleep(1)
print("Error, Session not authorized")
time.sleep(1)
passwords = [1290, 5098, 67572]
user_password = int(input("Enter access code(Must be IT Department level or higher): "))
for i in passwords:
    if user_password == i:
        employee_code = int(input("Enter employee code: "))
        Authorized(employee_code)
        break
else:
    print("Unauthorized Access!, Blocking session...")
    time.sleep(3)
    sys.exit()