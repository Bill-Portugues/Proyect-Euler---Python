
def Buscador_de_Primos(posicion):

    Primenum = [2]
    y = 2
    while len(Primenum) < posicion:
        for x in Primenum:
            if y%x ==0:
                break

            if x == Primenum[-1]:
                Primenum.append(y)
        y+=1

    print (Primenum.pop())


Buscador_de_Primos(10001)
#Buscador_de_Primos(6)