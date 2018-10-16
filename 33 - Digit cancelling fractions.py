def  FindingDig(min,max):

    results=[]

    for x in range(min,max,1):
        xS=str(x)
        if not '0' in xS and xS[0]!=xS[1]:

            for y in range(min, x , 1):
                xS = str(x)
                yS = str(y)
                if not '0' in yS and yS[0]!=yS[1]:

                    z=0
                    while xS.__len__() > 1 and z < 2:

                        w=0
                        while yS.__len__()>1 and w <2:
                            if xS[z] in yS[w]:
                                xS= xS.replace(xS[z],"")
                                yS= yS.replace(yS[w],"")

                                res=y/x

                                res2=int(yS) / int(xS)

                                if res==res2:
                                    results.append(res)
                                    print (y, x, res)

                            w+=1
                        z+=1
    return results

def previosWork():

    numbers = FindingDig(12,100)
    max=1

    for x in numbers:
        max *=x

    print ((1/max))

previosWork()