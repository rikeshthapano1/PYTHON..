import random

dice_roll = random.randint(1,6)

while True:
    user_input = input("Press 'r' to roll the dice or 'q' to quit : ")

    if user_input.lower()== 'r':
        print(f"You rolled a {dice_roll}!!")
        dice_roll = random.randint(1,6)

    elif user_input.lower() == 'q':
        print("Thanks for playing!!")
        break

    else:
        print("Invalid input. Please press r or q.")