a = "make a lot of money"
b = "buy now"
c = "subscribe this"
d = "click this"

comment = input("enter your comment :")

if(a in comment or b in comment or c in comment or d in comment  ):
    print("this is spam")

else:
    print("great comment")