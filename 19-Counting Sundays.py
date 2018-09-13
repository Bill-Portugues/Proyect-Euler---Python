

dia_mes=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def calculador (dia_sem, dia_ini_sem, año ):
    #dia_sem Domingos   $num_dia_target el primero de cada mes # dia_ini_sem  El año arranca en Miercoles

    qdias=0

    #Evaluamos la situacion inicial
    if dia_sem == dia_ini_sem:
        qdias +=1

    for x in range(0,len(dia_mes),1):
        dia_ini_sem += desplazamiento(qdias_x_mes(año, x)) #el %7 es para que siempre se quede en valores entre 1 y 7

        if dia_ini_sem > 7:
            dia_ini_sem = dia_ini_sem%7

        if dia_sem == dia_ini_sem and x != (len(dia_mes)-1):
            qdias += 1

    return qdias,dia_ini_sem


def qdias_x_mes(año,mes):
    #Cuantos dias tiene cada mes contemplando biciestos

    #si es biciesto
    if mes==1 and año%4==0:
        dias=29
    else:
        dias=dia_mes[mes]

    return dias

def desplazamiento(dias):
    #dia de la semana despues del desplazamiento de dias
    return (dias%7)


def Iterador_Años(año1,año2,dia_sem, num_dia_target, dia_ini_sem,):

    dia_ini_sem += desplazamiento(num_dia_target - 1)
    overall=0

    for x in range(año1,año2+1,1):
        dias_encontrados, dia_ini_sem = calculador(dia_sem, dia_ini_sem, x)
        overall +=dias_encontrados
        print (x,dias_encontrados)
    return overall

print (Iterador_Años(1901, 2000, 7, 1, 3)) #3 = Miercoles
