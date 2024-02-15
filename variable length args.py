def variable_length(*names):
    print(names)

num = int(input("Enter no. of entries: "))
a = 1
string1 = ""

while a <= num:
    string = input("Enter name: ")
    string1 = string1 + string
    a += 1

variable_length(string1)