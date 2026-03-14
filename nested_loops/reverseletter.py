for i in range(4,0,-1):
    for j in range(i+1):
        print(chr(65+j),end="")
    print()


for i in range(1, 5):                # 4 rows
    # print spaces
    for j in range(4 - i):
        print(" ", end="")

    # print increasing numbers
    for k in range(1, i + 1):
        print(k, end="")

    # print decreasing numbers
    for l in range(i - 1, 0, -1):
        print(l, end="")

    print()  # move to next line
