'''
a=input("Enter a word : ")
b=input("Enter a letter : ")
v = False
for i in a:
    if b.lower() == i.lower():
        print("Yes")
        v = True
        break
if not v:
    print("No")

a=int(input("Enter a number : "))
b=0
while b<a:
    b=b+1
    print(b*"*")

a=int(input("Enter a number : "))
b=a+1
while b>0:
    b=b-1
    print(b*"*")

import random
b=random.randint(0,10)
a=int(input("Enter a number : "))
while a!=b:
    a = int(input("Enter a number : "))
print("You guessed it rightt!")

a=int(input("Enter a number : "))
b=0
c=b
while b<a:
    b=b+1
    c=b+c
print(c)

def gcd(a,b):
    hcf = 1
    counter = 1
    while counter < a and counter < b:
        counter+=1
        if a % counter == 0 and b%counter == 0:
            hcf = counter
    return hcf
def lcm(a,b):
    c = max(a,b)
    while not (c%a==0 and c%b==0):
        c+=1
    return c


def forLoop(start,end,step=1):
    for i in range(start,end,step):
        print("*"*i)
        print("lalala")

def ForLoopInTermsOfWhile(start,end,step=1):
    i = start
    while i < end:
        print("*")
        print("lalala")
        i = i + step
forLoop(1,10)
ForLoopInTermsOfWhile(1,10)


a = 1
while a < 5:
    b = 1
    while b <= a :
        print(a,b)
        b+=1
    a += 1

for a in range(1,5):
    for b in range(1,a+1):
        print(a,b)
'''
a = {"ZING":"Hello"}
a["No"] = "Yes"
a["ZING"] = "HI"

print()





