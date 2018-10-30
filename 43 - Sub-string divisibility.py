import time
from itertools import permutations


def CheckSubString(num):

    xS=str(num)
    tests=[17,13,11,7,5,3,2]
    flag=True
    x=0
    z=8

    while x < tests.__len__() and flag==True:

        flag=Subcall(xS,z,z+2,tests[x])

        x+=1
        z-=1

    return flag


def Subcall(numStr,ini,fin,divisible):


    if int(numStr[ini-1:fin])%divisible==0: flag=True
    else: flag=False

    return flag


def final():

    all=[0,1,2,3,4,5,6,7,8,9]

    overall=[]

    long=all.__len__()

    Analysis=list(permutations(all[0:long], long))

    long2=len(Analysis)

    y=1

    while y <= long2:
        dato=int("".join(map(str, Analysis[long2-y])))

        if CheckSubString(dato):

            overall.append(dato)
        y+=1

    return overall


start = time.time()


print (sum(final()))

#print(CheckSubString(1406357289))

end = time.time()
print(end - start)