import random

for i in range(3):
    print(random.random())
    print(random.randint(10, 20))  # To print random integer between

members = ['Nidhi', 'Soumya', 'Arpita', 'Himanshi', 'Aryan']
leader = random.choice(members)
print(leader)
