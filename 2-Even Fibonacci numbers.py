# -*- coding: utf-8 -*-


'''[i for i in list if i.attribute == value]'''

Sumatoria = [1,2]

while True:

     for x in range(1,4000000):
        Resultado = (Sumatoria[x-1] + Sumatoria[x])
        if Resultado >4000000:
            break
        else:
            Sumatoria.append(Resultado)
     break

print (Sumatoria)
Sumatoria = [x for x in Sumatoria if x%2==0]
print (Sumatoria)
print (sum(Sumatoria))