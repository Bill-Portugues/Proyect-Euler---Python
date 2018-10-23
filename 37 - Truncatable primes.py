import time
import math


def FindingPrimesV1(numb):

    Primes=[2,3,5,7]
    Overall = []
    x=11

    while Overall.__len__()<11:

        raiz = math.sqrt(x)

        flag=True
        for y in range(0,Primes.__len__(),1):
            if Primes[y] > raiz:
                break
            elif x%Primes[y]==0:
                flag=False
                break
        if flag==True:
            Primes.append(x)
            if TruncablePrime(x,Primes): Overall.append(x)
        x+=2



    return Overall


def TruncablePrime(x,list):

        xS=str(x)
        largo=xS.__len__()

        cont = 1
        flag=True

        while cont<largo and flag:

            left=xS[cont:largo]
            right=xS[0:largo-cont]

            if not int(left) in list or not int(right) in list:
                flag=False

            cont+=1

        return flag

start = time.time()

print (sum((FindingPrimesV1(11))))


end = time.time()
print(end - start)