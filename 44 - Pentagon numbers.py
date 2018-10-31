
import time
import math

def Pentagon(num):

    Pentagon=[]
    last=0
    x=1

    while last <=num:

        last=int((x*(3*x-1)/2))
        Pentagon.append(last)
        x+=1

    return Pentagon

def SubRutine(num):

    flag=False
    x=(math.sqrt(1 + 24 * num ) + 1.0 )/ 6.0
    if x == int(x):
        flag=True

    return flag


def Check(Pent):

    minimo=10000000000

    for x in range(0,Pent.__len__(),1):
        for y in range(x+1, Pent.__len__(), 1):
            Sum=Pent[x] + Pent[y]
            Dif=Pent[y]-Pent[x]
            if SubRutine(Dif) and SubRutine(Sum):
                print (Pent[x],Pent[y],Dif,Sum)
                if Dif<minimo:
                    minimo=Dif

    return minimo



start = time.time()

print (Check(Pentagon(10000000)))


end = time.time()
print(end - start)