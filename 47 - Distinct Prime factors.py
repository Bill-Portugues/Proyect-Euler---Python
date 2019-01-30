import time
import math
from itertools import permutations
from functools import reduce


def FindingPrimesV1(numb,Primes):

    if Primes[-1]==2:
        iniciador=3
    else:
        iniciador=Primes[-1]+2

    for x in range(iniciador,numb,2):
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



def FactorizarNumero(Primes,EvaluatedNumber,):

    ListaFactorizada = []
    counter=0
    cuenta=1
    Primo = Primes[counter]
    Incambiable=int(EvaluatedNumber)

    while not cuenta==Incambiable  and not(counter==len(Primes)-1) :
        if EvaluatedNumber % Primo == 0:
            EvaluatedNumber = EvaluatedNumber/Primo

            cuenta *=Primo

            if len(ListaFactorizada) == 0:
                ListaFactorizada.append(Primo)

            elif ListaFactorizada[-1] %  Primo ==0:
                ListaFactorizada[-1]*=Primo

            else:
                ListaFactorizada.append(Primo)


        else:
            counter += 1
            Primo=Primes[counter]


    return ListaFactorizada




def final(target):

    flag=True

    EvaluatedNumber=13
    Primes=[2]
    QuantityPrimes=100000
    ListaRespuestaFinal = []
    ListaFactorizada = []
    counter = 0

    while flag:

        Primes=FindingPrimesV1(QuantityPrimes,Primes)

        Flow=True

        while not(ListaRespuestaFinal.__len__()==target):

            ListaFactorizada.append(FactorizarNumero(Primes,EvaluatedNumber))

            if len(ListaFactorizada[-1])==target:
                ListaRespuestaFinal.append(EvaluatedNumber)

            else:
                ListaRespuestaFinal=[]
                ListaFactorizada=[]

            counter+=1
            EvaluatedNumber+=1

        if ListaRespuestaFinal.__len__()==target:
            flag=False

    return ListaRespuestaFinal,ListaFactorizada

def PrintearRespuesta(ListaRespuestaFinal,ListaFactorizada):

    for x in range(0,ListaRespuestaFinal.__len__(),1):
        print ( ListaRespuestaFinal[x], "  = " , ListaFactorizada[x])


start = time.time()

ListaRespuestaFinal,ListaFactorizada = final(4)
PrintearRespuesta(ListaRespuestaFinal,ListaFactorizada)


end = time.time()
print(end - start)