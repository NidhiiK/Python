# try except constructor : to handle error

try:
    age = int(input("Age: "))
    print("Your age is " + str(age))
    income = 20000
    risk = income / age
    print(risk)

except ZeroDivisionError:
    # ZeroDivisionError : Nothing can be divided by zero
    print("Income cannot be divided by zero")

except ValueError:
    print("Invalid Input")
