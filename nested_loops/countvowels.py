sentence = input("Enter a sentence: ")
words = sentence.split()   # splits the sentence into a list of words

for word in words:
    count = 0
    for ch in word:
        if ch in "aeiouAEIOU":
            count += 1
    print(word, "→", count, "vowel" if count == 1 else "vowels")
