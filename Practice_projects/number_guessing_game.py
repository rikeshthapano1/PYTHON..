import random

computer_number = random.randint(1,100)

your_number = int(input("Guess a number between 1 and 100: "))

while True:
    if your_number < computer_number:
        print("Too low!! Try again.")

        your_number = int(input("Guess a number between 1 and 100:"))

    elif your_number > computer_number:
        print("Too high!! Try again.")

        your_number = int(input("Guess a number between 1 and 100:"))

    else:

        print("Congratulations!! You guessed the correct number as of computer!!")

        break

