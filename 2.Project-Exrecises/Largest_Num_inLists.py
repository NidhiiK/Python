numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for item in numbers:
    if (item > max):
        max = item
    # else:   --> The code works without this also
    #     item = item + 1

print(max)