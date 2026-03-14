import os

# specify the directory (use "." for current directory)
directory = "S:"

# list all files and folders
contents = os.listdir(directory)

# print them
print("Contents of directory:", directory)
for item in contents:
    print(item)
