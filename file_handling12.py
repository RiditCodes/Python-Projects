file = open(r"C:\Users\Ridit\OneDrive\Desktop\file2.txt", "r")

#print(file.readline())
#print(file.read())
lines = file.readlines()

print(type(lines))
print(lines)
file.close()