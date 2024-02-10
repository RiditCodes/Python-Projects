def variable_length(*names):
    print(type(names))
    for name in names:
        print(name)

num = int(input("Enter no. of entries: "))
a = 1
string1 = ""

while a <= num:
    string = input("Enter name: ")
    if a < num:
        string1 = string1 + string + ","
    else:
        string1 = string1 + string
    a += 1

variable_length(string1)
print()
variable_length("India","Bangladesh","Nepal")