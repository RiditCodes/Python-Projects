name = input("Enter your word: ")
eman = []
for n in range(len(name)-1,-1,-1):
    eman.append(name[n])
print(f"The reverse of your name is {eman}")
