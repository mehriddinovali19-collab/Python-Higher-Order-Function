people = [
  {"name": "Ali", "age": 25},
  {"name": "Sami", "age": 19},
  {"name": "Lola", "age": 31}
]

res = sorted(people, key=lambda x: x["age"])
print(res)