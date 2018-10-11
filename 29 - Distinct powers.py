
def  DistinctPowers(low,maxi):

    TotalList=[]

    for x in range (low,maxi+1,1):
        for y in range(low, maxi+1,1):
            TotalList.append( x ** y)

    return EliminarDuplicados(TotalList).__len__()

def EliminarDuplicados(lista):
    lista.sort()

    x=1

    while x <= len(lista)-1:

        while (lista[x-1]==lista[x]):
            lista.pop(x-1)

        x+=1
    return lista

print (DistinctPowers(2,100))