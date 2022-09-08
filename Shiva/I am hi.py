'''
taxCode=input("enter code : ")
price= int(input("enter price : "))
taxRate = 0.18
if taxCode == "T":
    price=(price*(1+taxRate))

opCode = int(input("enter code : "))

if opCode == 1 :
    x = float(input("enter number : "))
    y = float(input("enter number : "))
    print(x+y)

#x=int(input("enter a number : "))
def findArmstrong(x):
    sum=0
    for i in range(0,len(str(x))):
        sum+= ((x//(10**i))%10)**3
    #print(sum)
    if x == sum :
        print(x)



for i in range(1,1):
    findArmstrong(i)

'''

