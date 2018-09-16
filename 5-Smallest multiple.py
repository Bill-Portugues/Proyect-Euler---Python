

def primenum(inicio,fin):

    Final = [[x,0] for x in range(2,fin+1)]
    Sumafinal = 1

    for x in range(fin,inicio,-1):

        Resultados = []
        Factorizacion = range(2,x+1)
        Original = x


        for y in Factorizacion:
            while x%y ==0:
                Resultados.append(y)
                x=x/y

            if x==1:
                break


        for x in range(0,len(Final)):
            Total = Resultados.count(Final[x][0])

            if Total > Final[x][1]:
                Final[x][1]=Total


    for x in range(0,len(Final)):
        Sumafinal= Sumafinal * (Final[x][0] ** Final[x][1])


    print (Sumafinal)







primenum(1,20)