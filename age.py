age = int(input("Enter your age: "))

if age < 13:
    print("You are a child")
elif 13 < age < 18:
    print("You are a teenager")
elif age >= 18:
    if age >= 60:
        print("You are a senior citizen and you can vote in elections")
    else:
        print("You are an adult and you can vote in elections")
