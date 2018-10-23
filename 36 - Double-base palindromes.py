import math



def binary(numb):
    Nbin=[]

    while numb >0:

        if numb%2==0:
            Nbin.append(0)
        else:
            Nbin.append(1)


        numb = math.floor(numb/2)

    Nbin.reverse()

    return (Nbin)

def PalindromesBinar(Nbin,type):


    largo=Nbin.__len__()

    if largo<=1:flag=True

    elif largo ==2:
        if Nbin[0]==Nbin[1]: flag=True
        else:flag=False

    else:
        medio = int(largo/2)

        l1=Nbin[0:medio]

        if largo % 2 !=0: medio+=1
        l2=Nbin[medio:largo]

        if type=='s':
            l2=l2[::-1]

        else:
            l2.reverse()

        if l1==l2:
            flag=True
        else:
            flag=False

    return flag


def Overall(target):

    Sum=0
    Count=0

    for x in range(0,target,1):
        if PalindromesBinar(str(x),'s'):
            if PalindromesBinar(binary(x),'l'):
                print (x , binary(x))
                Sum+=x
                Count+=1

    print (Count)
    return Sum

    pass



print (Overall(1000000))
