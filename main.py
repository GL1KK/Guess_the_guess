import random

value_system = random.randint(1, 100)


while True:
    value = int(input("Enter your guess: "))
    
    if value_system == value:
        print("You win")
        break  
    elif value_system > value:
        print("The number guessed is higher")
    elif value_system < value:
        print("The number guessed is less")
    else:
        print("Try again!")
