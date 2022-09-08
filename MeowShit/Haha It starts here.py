

def haha(n):

    count = 0

    start = 0,0,0

    allValues = {}

    current = start

    while True:







def divide(amoeba,amoebaDict):
    if amoebaDict[amoeba] == 1:
        del amoebaDict[amoeba]

    else:
        amoebaDict[amoeba] -= 1

    babyAmoebae = ((amoeba[0]+1,amoeba[1],amoeba[2]),(amoeba[0],amoeba[1]+1,amoeba[2]),(amoeba[0],amoeba[1],amoeba[2]+1))

    for babyAmoeba in babyAmoebae:
        if babyAmoeba in amoebaDict:
            amoebaDict[babyAmoeba] += 1
        else:
            amoebaDict[babyAmoeba] = 1



