from enum import unique

num = [2, 2, 4, 6, 3, 6, 1]

unique = []

for item in num:
    if item not in unique:
        unique.append(item)
print(unique)
