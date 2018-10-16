import time
import math


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
    print (Primes.__len__())
    return Primes

def CircularPrime(list):

    Circular=[2,5]

    for x in range(0,list.__len__(),1):
        xS=str(list[x])


        if "2" in xS or "5" in xS:
            pass

        else:

            flag=True
            for y in range(0,xS.__len__(),1):

                xS=xS[1:(xS.__len__())]+xS[0]

                if not int(xS) in list:
                    flag=False
                    break

            if Circular.count(list[x])<1 and flag:
                Circular.append(list[x])
                #print (list[x])


    return Circular

start = time.time()

print (CircularPrime(FindingPrimesV1(1000000)).__len__())


end = time.time()
print(end - start)