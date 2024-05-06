file = open(r"C:\Users\Ridit\OneDrive\Desktop\file1.txt", "w")

lines = int(input("Enter no. of lines in file: "))

for i in range(0, lines):
    txt = input("Enter text to write to file: ")
    file.write(txt + "\n")