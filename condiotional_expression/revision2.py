#for grading marks

marks1 = int(input("enter marks of math :"))
marks2 = int(input("enter marks of science :"))
marks3 = int(input("enter marks of nepali :"))
marks4 = int(input("enter marks of social :"))
marks5 = int(input("enter marks of english :"))


total = marks1 + marks2 + marks3 + marks4 + marks5

print("your total is: ", total)

percentage = (total/500) * 100

print("you got ",percentage,"%")

if percentage >= 90:
    print("your grade is A+")

elif percentage >= 80:
    print("your grade is A")

elif percentage >= 70:
     print("your grade is B+")

elif percentage >= 60:
    print("your grade is B")

else:
    print("youre fAILED")
