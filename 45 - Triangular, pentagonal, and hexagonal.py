import time


def Generator (tipo,desde,cuantos):

    NumerosGenerados=[]

    for x in range(desde,cuantos,1):

        if tipo == "Triangle":
            NumerosGenerados.append(int(((x+1)*x)/2))
        elif tipo == "Pentagonal":
            NumerosGenerados.append(int(((3 * x - 1) * x) / 2))
        else:
            NumerosGenerados.append(int((2 * x - 1) * x))



    return NumerosGenerados

def limpiador(lista):

    if 0 in lista:
        lista.pop(lista.index(0))

    if 1 in lista:
        lista.pop(lista.index(1))

    return lista

def buscadorCoincidencias(list1,list2,list3,desde):

    answers=[]

    for x in list1[desde:]:
        if x in list2:
            if x in list3:
                answers.append(x)

    return answers

def indexes(list1,list2,list3,answer):

    index=[]

    index.append(list1.index(answer))
    index.append(list2.index(answer))
    index.append(list3.index(answer))

    return index

def organizador(quantity):

    Jumper=500

    Triangle=[]
    Pentagonal=[]
    Hexagonal=[]
    quantity+=2
    answers = []
    counter = 0

    while answers.__len__() < quantity:

        Triangle.extend(Generator("Triangle",counter * Jumper , Jumper * (counter + 1)))
        Pentagonal.extend(Generator("Pentagonal", counter * Jumper, Jumper * (counter + 1)))
        Hexagonal.extend(Generator("Hexagonal", counter * Jumper, Jumper * (counter + 1)))

        answers.extend(buscadorCoincidencias(Triangle,Pentagonal,Hexagonal,counter*Jumper))

        counter+=1

    for x in answers[2:]:
        indices=indexes(Triangle,Pentagonal,Hexagonal,x)

        print ("Answer --> ",x, " Triangle= ",indices[0], " Pentagonal= ",indices[1], " Hexagonal= ",indices[2],)


start = time.time()

organizador(2)

end = time.time()
print(end - start)