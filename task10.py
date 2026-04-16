text = ["apple", "34", "banana", "100", "abc", "75"]

res = filter(lambda x: x.isdigit(), text)
print(list(res))