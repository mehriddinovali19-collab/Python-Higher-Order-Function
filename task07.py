prices = ["$120", "$340", "$50", "$90"]
res = list(map(lambda x: int(x.replace("$", "")), prices))
print(res)