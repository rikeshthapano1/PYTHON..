for i in range(1, 6):           # outer loop → 5 rows
    for j in range(5 - i):      # print spaces before stars
        print(" ", end="")
    for k in range(i):          # print stars
        print("*", end="")
    print()                     # move to next line
