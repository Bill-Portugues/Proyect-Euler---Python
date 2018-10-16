

def Factorials():

    Fact=[1]

    for x in range(1,10,1):
        if x < 3:
            Fact.append(x)

        else:
            aux=1
            while x>1:
                aux*= x
                x-=1
            Fact.append(aux)

    return Fact

def calculator(NumS,Lib):
    aux=0
    for x in range(0,NumS.__len__(),1):
        aux += Lib[int(NumS[x])]

    return aux

def  Search(Lib):

    Results=[]

    for x in range(1,100000):
        xS=str(x)

        flag=True

        if "5" in xS and xS.__len__()<3:
            flag=False

        if "7" in xS and xS.__len__() < 4:
            flag = False

        if "8" in xS and xS.__len__() < 5:
            flag = False

        if "9" in xS and xS.__len__() < 6:
            flag = False

        if flag==True:
            if calculator(xS,Lib) == x:
                Results.append(x)


    return Results

print(Search(Factorials()))