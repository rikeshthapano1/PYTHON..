# snake = 1 , water = 0 and gun = - 1


import random


def play():

    computer = random.choice([1,0,-1]) # computer le random choice garna sakne options haru, jasma 1 snake, 0 water, ani -1 gun ho.

    youch = input("Enter your choice (s/w/g): ") # user le input garna sakne options haru, jasma s snake, w water, ani g gun ho.

    game = {"s":1, "w":0, "g":-1} # game dictionary, jasma key haru user le input garna sakne options haru ho, ani value haru computer le random choice garna sakne options haru ho.
    revgame = {1:"Snake", 0:"Water", -1:"Gun"} # revgame dictionary, jasma key haru computer le random choice garna sakne options haru ho, ani value haru user le input garna sakne options haru ho, jasma 1 snake, 0 water, ani -1 gun ho.

    you = game[youch] # user le input gareko option lai game dictionary ko key sanga match garera computer le random choice garna sakne options haru ko value ma convert garne ho.

    print(f"You chose {revgame[you]}")
    # computer le random choice garna sakne options haru ko value lai revgame dictionary ko key sanga match garera user le input garna sakne options haru ma convert garne ho.
   
   
    print(f"Computer chose {revgame[computer]}")
    # computer le random choice garna sakne options haru ko value lai revgame dictionary ko key sanga match garera user le input garna sakne options haru ma convert garne ho.


    if computer == you:
        print("Draw")
        return "draw"

    elif (computer == 1 and you == 0) or (computer == 0 and you == -1) or (computer == -1 and you == 1):
        print("Computer Wins")
        return "computer"

    else:
        print("You Win")
        return "you"


your_score = 0
computer_score = 0


for i in range(10):

    print(f" \n Round {i+1}:")
    result = play()
    if result == "you":
        your_score += 1
    elif result == "computer":
        computer_score += 1
    elif result == "draw":
        pass

print(f"Your score: {your_score}")
print(f"Computer's score: {computer_score}")
print(f"you both have drawn {10 - (your_score + computer_score)} times.")

print("\nFinal Result:")
if your_score > computer_score:
    print("Congratulations! You won the game!")
elif your_score < computer_score:
    print("Computer wins the game! Better luck next time.")
else:
    print("It's a draw! Well played.")