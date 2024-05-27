file = open(r"C:\Users\Ridit\OneDrive\Desktop\file2.txt", "a+")

number = int(input("Enter number of lines: "))

i = 1
string1 = ""

while i <= number:
    string = input("Enter string: ")
    string1 = string1 + "\n" + string
    i += 1

file.write(string1)

file.seek(0)

print(file.read())

file.close()