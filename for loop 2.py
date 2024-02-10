even_or_odd = input("Press E for even and O for odd: ")
if even_or_odd == "E":
    for number in range(0, 101, 2):
        print(number)
if even_or_odd == "O":
    for number in range(1, 101, 2):
        print(number)
# num%2!=0
