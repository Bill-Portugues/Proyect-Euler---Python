import time

LookUp=[10,100,1000,10000,100000,1000000]

LookUp2=[9,10,11,12,99,1000]

def Calculate_Irrational_digit(num):

    dict=[]
    sum = 0
    for x in range(1,num):
        for y in range(0,str(x).__len__(),1):
            sum+=1
            dict.append(int(str(x)[y]))
            #print (sum,"-",str(x)[y])


    return dict


def Overall(lista):

    dict=Calculate_Irrational_digit(max(lista))

    sum=1

    for x in range(0,lista.__len__(),1):
        print (lista[x],"--",dict[lista[x]-1])
        sum *= dict[lista[x]-1]

    return sum


start = time.time()

print (Overall(LookUp))

end = time.time()
print(end - start)


