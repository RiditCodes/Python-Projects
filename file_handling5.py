file = open(r"C:\Users\Ridit\OneDrive\Desktop\file2.txt", "w")
list = []

lines = int(input("Enter no. of lines: "))

for i in range(0, lines):
    txt = input("Enter text: ")
    list.append(txt + "\n")

file.writelines(list)
file.close()