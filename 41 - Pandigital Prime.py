import time
import math
from itertools import permutations

def pand(num):
    flag=True
    xS=str(num)

    for x in range(1,xS.__len__()+1,1):
        if xS.count(str(x))!=1:
            flag=False

    return flag



def FindingPrimesV1(numb):

    Primes=[2]

    for x in range(3,numb,2):
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

    return Primes


def CheckPrime(num,primes):

    flag=True

    raiz = math.sqrt(num)

    for y in range(0,primes.__len__(),1):
        if primes[y] > raiz:
            break
        elif num%primes[y]==0:
            flag=False
            break

    return flag


def final(primes):

    all=[1,2,3,4,5,6,7,8,9]


    flag=True

    long=all.__len__()

    answer=0
    x=0

    while flag and x <long:
        Analysis=list(permutations(all[0:long-x], long-x))

        long2=len(Analysis)

        y=1
        while flag and y <= long2:
            dato=int("".join(map(str, Analysis[long2-y])))


            if not dato%2==0:
                if CheckPrime(dato,primes):

                    if pand(dato):
                        flag=False
                        answer=dato
            y+=1

        x+=1
    return answer


start = time.time()

#print (list(permutations([1, 2, 3, 4], 4)).__len__())

#Dado que para verificar si un numero es primo se necesita iterar por todos los primos menores a raiz del primo en busqueda,
#  solo necesito tener almacenados los primos menores a Raiz del numero mas grande posible (987654321)
print (final(FindingPrimesV1(math.ceil(math.sqrt(987654321)))))


end = time.time()
print(end - start)