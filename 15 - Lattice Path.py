import numpy

def Paths(num):

    PathTot = numpy.zeros((num+1,num+1))
    Next=[]
    Trace=[]


    # STARTERS VALUES
    Original=[num,num]
    Voriginal = 1
    Aux=Neighbours(Original)

    while Aux.__len__()>0:
        while Aux.__len__()>0:

            PathTot[Aux[0][0]] [Aux[0][1]] +=Voriginal
            D=Aux.pop(0)
            if not D in Trace and not D in Next:
                Next.append(D)

        Original=Next.pop(0)
        Trace.append(Original)
        Voriginal = int(PathTot[Original[0]][Original[1]])
        Aux=Neighbours(Original)


    print (PathTot)
    return PathTot[0][0]





def Neighbours(List):

   # print (List)
    Neig=[]
    x=List[0]
    y=List[1]

    #Izquierda
    if x-1 >=0:
        Neig.append([x-1,y])

    # Arriba
    if y - 1 >= 0:
        Neig.append([x, y-1])

    return Neig




print ("\n Resultado = " , int(Paths(20)))