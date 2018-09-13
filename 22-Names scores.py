
def reading():

    overall =0
    with open("Ejercicio22.txt", "r") as filestream:
        for line in filestream:
            currentline = line.split(",")
            currentline.sort()
            for x in range (0,currentline.__len__(),1):
                overall += (letter_score(currentline[x]) * (x+1))
                print (x,currentline[x],overall)

    return overall



def letter_score(palabra):

    palabra=palabra[1 : (palabra.__len__()-1)]


    x=[ord(c)-64 for c in palabra]

    print(palabra,x,sum(x))
    return sum(x)

print (reading())