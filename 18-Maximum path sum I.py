

T=[75,95, 64,17, 47, 82,18, 35, 87, 10, 20, 4, 82, 47, 65, 19, 1,23, 75, 3, 34,88, 2, 77, 73, 7, 63, 67, 99, 65, 4,
   28, 6, 16, 70, 92,41, 41, 26, 56, 83, 40, 80, 70, 33,41, 48, 72, 33, 47, 32, 37, 16, 94, 29,53, 71, 44, 65, 25, 43,
   91, 52, 97, 51, 14,70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57,91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48,
   63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31, 4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]

T2=[3,7,4,2,4,6,8,5,9,3]

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


Tablero = Triangulo(T,14)

Tablero.MaxTree()

print (Tablero.nod[0].value)

