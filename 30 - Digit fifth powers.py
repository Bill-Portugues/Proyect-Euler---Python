
def  DigitFifth(low,maxi,power):

    TotalList2=[]
    li=[2, 5, 9, 8]
    suma=0

    for x in range (low,maxi+1,1):
        suma = 0

        for y in range(0, str(x).__len__(),1):
            suma += int(str(x)[y]) ** power

        if x == suma:
            print (x)
            TotalList2.append(x)

    return sum(TotalList2)


print (DigitFifth(2,1000000,5))