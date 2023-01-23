from itertools import groupby

num = input()

for key, group in groupby(num):
    print(f"({len(list(group))},  {str(key)})", end=" ")
