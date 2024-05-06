file = open(r"C:\Users\Ridit\OneDrive\Desktop\file2.txt", "a")

txt = input("Enter string to append to file: ")

file.write(txt + "\n")
file.close()