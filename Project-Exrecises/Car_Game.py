print("Enter help to understand the game")
help = input()

if help == 'help' or 'HELP':
    print('start - to start the car')
    print('stop  - to stop the car ')
    print('quit  - to exit')
else:
    print('Enter a valid Command')

car_command = input('Enter the command for car: ')

if car_command == 'start':
    print('Car started...Ready to go?')
elif car_command == 'stop':
    print('Car stopped')
elif car_command == 'quit':
    print('Game over')
else:
    print("I don't understand that...")
