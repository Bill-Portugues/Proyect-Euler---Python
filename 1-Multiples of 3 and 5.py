# -*- coding: utf-8 -*-


Numeros = range(1,1000)
Sumatoria = []


'''for x in Numeros:
    if any([x % 3 == 0, x % 5 == 0]):
        Sumatoria.append(x)
  '''
Sumatoria = [x for x in Numeros if any([x % 3 == 0, x % 5 == 0])]

print (sum(Sumatoria))
print (Sumatoria)



