
word = input("enter a word :")
count = 0

for ch in word:
    if ch in "aeiou":
        count +=1
print("there are" ,count, "vowels")

