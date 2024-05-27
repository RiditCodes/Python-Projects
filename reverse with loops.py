name = input("Enter your word: ")
list = []
eman = ""
for n in range(len(name)-1,-1,-1):
    list.append(name[n])

eman = "".join(list)
print(f"The reverse of your name is {eman}")