import time

def reading(base):


    overall =0

    with open("Ejercicio 42.txt", "r") as filestream:
        for line in filestream:
            currentline = line.split(",")
            currentline.sort()
            for x in range (0,currentline.__len__(),1):
                if letter_score(currentline[x]) in base:
                    overall+=1

    return overall



def letter_score(palabra):

    palabra=palabra[1 : (palabra.__len__()-1)]


    x=[ord(c)-64 for c in palabra]

    #print(palabra,x,sum(x))
    return sum(x)


def Triangle(num):

    Triangles=[]
    last=0
    x=1

    while last <=num:

        last=int((x/2*(x+1)))
        Triangles.append(last)
        x+=1

    return Triangles

#La palabra mas larga tiene 16 caracteres y el valor maximo por letra es de la z = 27 ,
#Podemos generar una lista que contenga todos los valores hasta 27*16=432





start = time.time()


print (reading(Triangle(27*16)))

end = time.time()
print(end - start)