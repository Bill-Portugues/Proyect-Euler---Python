
def Pandigital(numb):

    # El número fijo mas alto estara dado por uno que se multiplique por 2, ya que 1 daría numeros repetidos

    # El numero que multipliquemos debe tener 4 digitos y al multiplicarlo, el producto debe tener 5 digitos

    # A partir del numero fijo 5000, al multiplicarlo por 2 , se obtienen 5 digitos, el máximo para mantener los 4 digitos de condicion es 9999

    #Ajustamos ligeramente el minimo y el máximo ya que no se pueden repetir caracteres



    for x in range(9876,5123,-1):
        y=x*numb
        if Pand(str(x) + str(y)):
            return str(x) + str(y)

    # Lo hacemos correr al reves ya que de hallar el resultado, es el final, no hace falta verificar mas

def Pand(numb):
    x=1
    flag=True

    while x <=9 and flag == True:

        if not numb.count(str(x))==1:
           flag=False

        x+=1

    return flag

print (Pandigital(2))