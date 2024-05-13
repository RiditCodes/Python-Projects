file = open(r"C:\Users\Ridit\OneDrive\Desktop\file2.txt", "r+")

print(file.read())
file.write(input("Enter a string: "))

file.close()
#r+ mode supports write function while r mode does not