
def  SpiralWaves(number):

    layers=int((number+1)/2)

    OriginalNum=1

    sum=1

    step=2

    for x in range(1,layers,1):

        for y in range(1,5,1):
            sum += OriginalNum + step*y

        OriginalNum += step*4
        step+=2

    print (sum)


SpiralWaves(1001)