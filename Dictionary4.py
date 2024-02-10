a = ("key1", "key2", "key3")
b = 0

dictionary = dict.fromkeys(a, b)
print(dictionary)

dictionary.pop("key2")
print(dictionary)

dictionary.popitem()
print(dictionary)

dictionary.update({"key4":4})
print(dictionary)