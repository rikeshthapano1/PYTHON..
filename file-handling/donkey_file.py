word = "monkey"

f = open("donkey_file.txt", "r")
content = f.read()
f.close()

New_content = content.replace(word, "monkey" )
f = open("donkey_file.txt", "w")
f.write(New_content)
f.close()