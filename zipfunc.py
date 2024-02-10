#zip() function combines two lists.

company = ["Raspberry Pi", "Microsoft", "Apple"]
no_of_employees = [800, 1000, 500]

result = {company : no_of_employees for company, no_of_employees
    in zip(company, no_of_employees)}

print(result)

company1 = []
no_of_employees1 = []

#Extracting Dictionary keys

for key in result.keys():
    company1.append(key)

#Extracting Dictionary values

for key in result.keys():
    no_of_employees1.append(result[key])

print(company1)
print(no_of_employees1)