

def Evaluator(test):

    test=str(test)
    testseparado = [x for x in test]
    status = False

    largo = len(testseparado)
    if largo%2 != 0:

        testseparado.pop((largo // 2))
        largo -=1


    for x in range(0,largo//2):
        if testseparado[x] == testseparado[largo-1-x]:
            status = True
        else:
            status = False
            break

    return status


def randomnum(digitos):
    max=9
    min=1
    numerosmax =0

    minimo=int(str(min)*digitos)
    a=int(str(max)*digitos)
    b = a



    for x in range(a,minimo,-1):
            for y in range(a,minimo,-1):
                if Evaluator(x*y) == True:
                    if numerosmax<(x*y):
                        numerosmax = (x*y)

    return numerosmax

print (randomnum(3))