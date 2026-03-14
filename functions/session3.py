# celcius to fahrenhiet

def CtoF(f):
    c = 5* (f-32)/9

    return c
 
f = int(input("enter your temparature : "))

print(round(CtoF(f),2), "C")
