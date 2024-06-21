set1 = {"A", "B", "C"}
set2 = {"B", "D", "E"}
set3 = {"C", "F", "G"}

print(set1.difference(set2, set3))
print(set2.difference(set1, set3))
print(set3.difference(set1, set2))