Days1 = {"Monday", "Tuesday", "Wednesday"}
Days2 = {"Wednesday", "Thursday"}
Days3 = {"Friday", "Wednesday"}

#Days1.intersection_update(Days2, Days3)
Days2.intersection_update(Days1, Days3)

print(Days1)
print(Days2)
print(Days3)