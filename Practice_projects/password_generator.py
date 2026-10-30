
import string
import random

char_pool = string.ascii_letters + string.digits + string.punctuation #string.punctuation le special characters haru lai include garxa ani ascii_letters le upper case ra lower case letters haru lai include garxa ani digits le number haru lai include garxa

random_char = random.choices(char_pool,k=8) #k is the length of password normally 8 to 12 hunxa so 8 rakham





for i in random_char:
    print( i,end="",)
    
print (f" \n you can use this password") 