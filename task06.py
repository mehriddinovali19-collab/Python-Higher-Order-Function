emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]
res = list(filter(lambda x: x.endswith("gmail.com"), emails))
print(res)