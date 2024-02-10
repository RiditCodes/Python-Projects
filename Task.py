rows = 9
num = 0
spaces = 0
spaces2 = 0
for r in range(0, rows):
    for s in range(1, (rows-r)+1):
        print("  ", end="")
        spaces+=1

    while num!=((2*r)-1):
        if spaces<=rows-1:
            print(r+num, end=" ")
            spaces+=1
        else:
            spaces2+=1
            print(r+num-(2*spaces2), end=" ")
        num += 1

plan =''' 1
        2 2 2
      3 3 3 3 3
    4 4 4 4 4 4 4
  4 * * * * * * * *
* * * * * * * * * * *
 '''