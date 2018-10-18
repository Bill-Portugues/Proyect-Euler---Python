

def Reading(filex):
    rows = []
    FILE = open(filex, "r")
    Tot=[]

    for num in FILE: rows.append([int(i) for i in num.split(" ")])

    for x in range(0,rows.__len__(),1):
        for y in range(0,rows[x].__len__(),1):
            Tot.append(rows[x][y])

    return Tot



class Triangulo:
    def __init__(self, List, Height):
        self.H = Height
        self.items = List
        self.long =List.__len__()
        self.nod = [None] * self.long
        self.Nodes()
        self.Children()

    def Nodes(self):

        for x in range(0,self.long,1):
            self.nod[x] = Nodo(x,self.items[x])

    def Children(self):
        w=0
        for level in range(0, self.H+1, 1):
            for y in range(0, level + 1, 1):

                self.nod[w].level = level
                if not level==self.H:

                    self.nod[w].left = self.nod[w +level +1]
                    self.nod[w].right = self.nod[w +level+2]
                w+=1





    def MaxTree(self):
        initial=self.long-(self.H+2)

        while initial >=0:
            if (self.nod[initial].left).value > (self.nod[initial].right).value:
                self.nod[initial].value += self.nod[initial].left.value

            else:
                self.nod[initial].value += self.nod[initial].right.value


            initial-=1



    def SumPath(self):

        for x in range(0,self.H+1,1):

            if self.nod[x].left>self.nod[x].right:
                sum += self.nod[x].left
            else:
                sum += self.nod[x].right

        return sum






class Nodo(Triangulo):
    def __init__(self,element,value):
        self.index=element
        self.level=None
        self.left=None
        self.right=None
        self.value = value

    def SumLeft(self,sum):

        if self.left==None:
            sum += self.value
            return sum

        else:
            sum += self.value
            sum=self.left.SumLeft(sum)

        return sum

    def SumRight(self, sum):

        if self.right==None:
            sum += self.value
            return sum

        else:
            sum += self.value
            sum=self.right.SumRight(sum)

        return sum





#Tablero = Triangulo(T2,3)


Tablero = Triangulo(Reading('Ejercicio 67.txt'),99)

# 'C:\Users\Lucas\PycharmProjects\Proyect_Euler\Ejercicio 67'

Tablero.MaxTree()

print (Tablero.nod[0].value)

