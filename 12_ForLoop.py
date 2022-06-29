for item in 'Python':
    print(item)

for item in ["Nidhi", "Soumya"]:
    print(item)

for num in range(2, 20):
    print(num)

for num in range(2, 20, 2):  #This will alternate numbers, i.e skipping 2 no.s
    print(num)

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price
print(f"Total: {total}")