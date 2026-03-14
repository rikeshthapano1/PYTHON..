from collections import Counter

marks   = []

f = int(input("enteryour marks :"))
marks.append(f)

f1 = int(input("enter your marks:"))
marks.append(f1)
f2= int(input("enter your marks:"))
marks.append(f2)
f3 = int(input("enteryour marks :"))
marks.append(f3)
f4 = int(input("enter your marks:"))
marks.append(f4)
f5 = int(input("enter your marks:"))
marks.append(f5)
f6 = int(input("enter your marks:"))
marks.append(f6)

marks.sort()

print((marks))

marks.insert(4,55)

print(marks)

print(Counter(marks))