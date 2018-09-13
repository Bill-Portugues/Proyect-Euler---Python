def Amicable(number):

    list_primes_powers=[]
    list_divisors = []
    original=number

    flag = 1
    x=2

    while int(number)!=flag:

        y=1
        while number%x==0:

            if y==1:
                if x!=original:
                    list_primes_powers.append([x])
                    list_divisors.append(x)
            else:

                if x**y != original:
                    list_primes_powers[list_primes_powers.__len__() - 1].append(x ** y)
                    list_divisors.append(x**y)
            number /= x
            y+=1
        x+=1

    list_divisors = different_approach(list_divisors,original)
    list_divisors.append(1) # adding the one that was excluded
    return list_divisors


def different_approach(listapotencias,number):


    len=listapotencias.__len__()

    x=0
    while x!=listapotencias.__len__():

        listprimitiva = []
        for y in range(x,len,1):
            listprimitiva.append(listapotencias[y] * listapotencias[x])

        for z in range(0,listprimitiva.__len__(),1):

            value=listprimitiva[z]

            if not listapotencias.count(value) > 0 and not value >= number and not number % value != 0:
                listapotencias.append(value)
        x+=1
        len = listapotencias.__len__()

    return listapotencias


def integrated(number1,number2):
    overall=0
    overall2=0
    for x in range(number1,number2,1):
        ida=sum(Amicable(x))
        if x == sum(Amicable(ida)) and ida != x:
            overall+=1
            overall2 +=x
            print ("Amicable",x)

    return overall, overall2



print (integrated(1,100000))



