

def cuadradoslocos(inicio,fin,potencia):

    sumatoria2 = 0
    desumatoria = 0

    for x in range(inicio,fin+1):
        sumatoria2=sumatoria2+ x ** potencia
        desumatoria = desumatoria + x

    print (sumatoria2)
    print (desumatoria ** potencia)
    print  ((desumatoria ** potencia) - sumatoria2)

cuadradoslocos(1,100,2)