a = ["sudesh", "rikesh", "harry", "ron"]

b = input("enter your name: ")

if b.lower() in [name.lower() for name in a]:
    print("your name is in the list")
else:
    print("your name is not in the list")
