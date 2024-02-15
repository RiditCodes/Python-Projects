def variable_length(names):
    print(names)

num = int(input("Enter no. of entries: "))
a = 1
string1 = ""

while a <= num:
    string = input("Enter name: ")
    if a == num:
        string1 = string1 + string
    else:
        string1 = string1 + string + ","
    a += 1

variable_length(string1)