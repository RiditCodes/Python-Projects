def recursive():
    global i
    if i < 5:
        i += 1
        recursive()
    
    print("Recursive function")

i = 0
recursive()