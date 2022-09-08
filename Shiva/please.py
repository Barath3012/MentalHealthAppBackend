import math
def find_num(w,wmax):
    lis = []
    for i in w:
        lis.append((int(wmax/i)+1))
    return (lis)
'''
def find_key(dict,val):
    for i in dict.keys():
        if dict[i] == val:
            return i
            break
'''
glodict={}
def max_val(w,v,wmax,maxnums,num,wt_left,value):

    if num != -1:
        emp = {}
        for i in range(0,maxnums[num]):
            if wt_left >= i * w[num]:
                emp[i] = (max_val(w,v,wmax,maxnums,num-1,wt_left-i*w[num],value+i*v[num]))
            else:
                emp[i] = max_val(w,v,wmax,maxnums,num-1,wt_left,value)
        a = max(emp.values())
        #b = find_key(emp,a)
        #lis.append(str(num)+': b')
        return (a)
    if num == -1:
        return (value)

def fn(w,v,wmax):
    maxnums = find_num(w,wmax)
    return max_val(w,v,wmax,maxnums,len(w)-1,wmax,0)


w = [2,3,5]
v = [1,3,6]

a = fn(w,v,wmax)
print(a)
