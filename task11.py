nums = list(range(1, 21))
res = list(map(lambda x: x **2, filter(lambda x: x % 2 ==0, nums)))
print(res)