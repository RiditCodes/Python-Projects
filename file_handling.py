'''The file "file1.txt" is automatically stored in the 
location where this python file is saved'''

file = open("file1.txt", "w")
file.write("File is opened in write mode")
file.close()