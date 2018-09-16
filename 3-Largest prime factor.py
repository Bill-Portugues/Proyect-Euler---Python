# -*- coding: utf-8 -*- 600851475143

objetivo = 600851475143
Sumatoria =[]

x=2
while x<=objetivo:

    Condicion = True
    if x > objetivo:
        print ('fin')
        break

    while Condicion:
        if objetivo % x == 0:
            Sumatoria.append(x)
            objetivo = objetivo / x
        else:
            Condicion = False

    if x %2 == 0:
        x+=1
    else:
        x+=2




print (Sumatoria)
print (max(Sumatoria))
print ('Termino')
