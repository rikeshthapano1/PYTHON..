count = 0

while True:
    word = input("enter a word ('stop' to stop the loop) :")

    if word == "stop":
        break
    count += 1

print("you entered",count,"words")