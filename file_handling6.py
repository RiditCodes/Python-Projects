file = open(r"C:\Users\Ridit\OneDrive\Desktop\file2.txt", "w")

num = int(input("Enter no. of lines:"))
List1 = []

for i in range(num):
    string = input("Enter string: ")
    List1.append(string + "\n")
    file.writelines(List1)

file.close()