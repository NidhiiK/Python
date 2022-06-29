birth_year = input('Birth year: ')
print(type(birth_year))
age = 2022 - int(birth_year)

#Here int(_) will convert the birth year which was in string to integer.

# print('Your age is ' + age) This will get error because only two strings can be concatenated and not a string and a integer
print(type(age))
print(age)