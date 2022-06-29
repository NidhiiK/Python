# with keyword argument, order of prameters doesn't matter. It matters in positional argument, in which we simply pass the value for parameters.
#   keyword argument shouls always come after positional argument.


def greet_user(first_name, last_name):

    print(f"Hi {first_name}{last_name}!")
    print('Welcome Aboard')


print("Start")
greet_user(first_name="Nidhi", last_name="Kumari")  # Keyword argument
greet_user("Nidhi", last_name="Kumari")
#   keyword argument should always come after positional argument.

print("Finish")
