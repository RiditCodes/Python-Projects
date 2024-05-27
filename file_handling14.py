file = open(r"C:\Users\Ridit\OneDrive\Desktop\file2.txt", "r")

space_count = 0
word_count = 0
len_file = 0
num_lines = 0
while True:
    char = file.read(1)
    if char == "\n":
        num_lines += 1
    elif char == "":
        break
    elif char == " ":
        space_count += 1
        word_count += 1
    else:
        len_file += 1

len_file += space_count
    
print(f"No. of characters: {len_file}")
print(f"No. of spaces: {space_count}")
print(f"No. of words in file: {word_count + num_lines + 1}")
print(f"No. of lines in file: {num_lines+1}")