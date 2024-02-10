unit = int(input("How many units of electricity did you use: "))
if unit <= 10:
    print("Your electricity bill is 50 Rupees")
elif unit > 10 and unit <= 50:
    print(f"Your electricity bill is {50+(unit-10)*4}")
elif unit > 50:
    print(f"Your electricity bill is {50+(unit-10)*4+(unit-50)*10}")
