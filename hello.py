import random

magic_number = random.randint(0, 10)

def game():
    user_number = int(input("Enter a number between 0 and 10. "))
    if user_number > 10 or user_number < 0:
        print("Please make sure the number is between 0 and 10")
    elif user_number == magic_number:
        print("You've won a magnificent prize! Virtual Hi-Five!")
    else:
        print("No luck. Please try again...")

game()