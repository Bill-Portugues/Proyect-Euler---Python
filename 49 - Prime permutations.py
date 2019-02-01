import time
import math
import bisect

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

class PrimosTrabajables:
    def __init__(self, Number):
        self.Number=Number
        self.Mapping=self.getMpapping(Number)

    def getMpapping(self,Number):

        Desagregado = [0] * 10

        NumberString=str(Number)

        for x in NumberString:
            Desagregado[int(x)] = NumberString.count(x)

        return Desagregado

    def compararCotroElemento(self,elemento2):

        answer=False

        if elemento2.Mapping==self.Mapping and self.Number!=elemento2.Number:
            answer=True

        return answer

    def compararSumas(self,elementos):

        diferencia = self.Number - elementos[0].Number
        answer=True

        for x in range(0,len(elementos)-1,1):

            if diferencia != elementos[x].Number - elementos[x+1].Number:
                answer=False
                break

        return answer


def Verificar2(quantity,Primes):

    ListaElementosPrimos = []

    for x in Primes:
        ListaElementosPrimos.append(PrimosTrabajables(x))

    counter=0
    answer=[]

    while answer.__len__() < quantity:
        for x in range(0,ListaElementosPrimos.__len__(),1):
            for y in range(x+1,ListaElementosPrimos.__len__(),1):
                if ListaElementosPrimos[x].compararCotroElemento(ListaElementosPrimos[y]):
                    for z in range(y+1,ListaElementosPrimos.__len__(),1):
                        if ListaElementosPrimos[x].compararCotroElemento(ListaElementosPrimos[z]) and\
                                ListaElementosPrimos[x].compararSumas([ListaElementosPrimos[y],ListaElementosPrimos[z]]):
                            answer.append([ListaElementosPrimos[x].Number,ListaElementosPrimos[y].Number,ListaElementosPrimos[z].Number,ListaElementosPrimos[z].Number - ListaElementosPrimos[y].Number])


    return answer


def organizador(quantity):



    #Generar todos los primos de 4 cifras:
    Primes=FindingPrimesV1(9999,[2])
    bisect.insort(Primes,1000)
    Primes=Primes[Primes.index(1000)+1:]

    #Verificar cual de todos ellos son permutaciones entre si

    answer=Verificar2(quantity,Primes)

    for x in answer:
        print ("Increases of: ",x[3], "Elementos: ",x[0],"-",x[1],"-",x[2])


start = time.time()


#print (Verificar2(1,[1487, 4817, 8147]))

organizador(2)


end = time.time()
print(end - start)