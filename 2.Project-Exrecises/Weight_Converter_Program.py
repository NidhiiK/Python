weight = int(input('Weight: '))
units = input("(L)bs or (k)g: ")

if units == 'p' or 'P':
    converted = weight / 0.45
    print(f"You are {converted} kilos")

elif units == 'k' or 'K':
    converted = weight * 0.45
    print(f"You are {converted} pounds")

else:
    print("Enter a valid unit of weight")
