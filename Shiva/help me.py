
no=1
glodict = {0:1,1:1}
def awoo(num):
    global no
    print(no)
    no+=1
    if num not in glodict:
        glodict[num] = awoo(num-1) + awoo(num-2)
    return glodict[num]
a = awoo(10)
print(a)