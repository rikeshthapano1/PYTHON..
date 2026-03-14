math = int(input("enter your math marks :"))
science = int(input("enter your science marks :"))
english = int(input("enter your english marks :"))

total = ((math+science+english)/300)*100

if(total>=40 and math>=33 and science>=33 and english>=33):
    print("you have passed", total)

else:
    print("you have failed",total)