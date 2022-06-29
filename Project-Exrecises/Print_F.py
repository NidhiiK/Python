numbers = [5, 2, 5, 2, 2]

for item in numbers:
    print('x' * item)

    #or

for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

num = [1, 1, 1, 1, 5]
for item in num:
    print('x' * item)