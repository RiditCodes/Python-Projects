import datetime

# get current date
current_date = datetime.date.today()
file = open(r"calendar.txt", "a")

print(f"Today is {current_date}")
go = input("Did you(or will you) go to table tennis today? Y for yes, N for no: ").lower()
if go == "n":
    file.write(f"\n{current_date}: No tennis");
else:
    file.write(f"\n{current_date}: Tennis")

file.close()