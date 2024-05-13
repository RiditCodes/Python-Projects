file = open(r"C:\Users\Ridit\OneDrive\Desktop\file1.txt", "w+")

txt = input("Enter a string: ")
file.write(txt)

file.seek(0)

read_file = file.read()
print(read_file)

file.close()