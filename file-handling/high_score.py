import random 

def game():

    print("You are playing the high score game. . .")
    score = random.randint(0,100)

    f = open("high_score.txt", "r")

    high_score = f.read()

    if  high_score != "" :
        high_score = int(high_score)
    else:
        high_score = 0

    if score > high_score:
        print(f"Congratulations! You have the new high score: {score}")
        f = open("high_score.txt", "w")
        f.write(str(score))
        f.close()
    
    else:
        print(f"Your score is {score}. The current high score is {high_score}. Better luck next time!")

game()


        
    

    
    