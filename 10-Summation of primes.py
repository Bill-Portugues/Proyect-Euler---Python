
import math

def Buscador_de_Primos(number):

    Primenum = [2,3,5,7]
    y = 9
    while y < number:

        for x in Primenum:
            if y%x ==0:
                break


        if x == Primenum[-1]:
            Primenum.append(y)


        y+=2
        if 5 == int(repr(y)[-1]):
            y+=2

    print (sum(i for i in Primenum))


Buscador_de_Primos(2000000)
#Buscador_de_Primos(6)