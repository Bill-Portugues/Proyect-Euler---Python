def Analysis(min1,max1,min2,max2):

    max=10000
    Results=[]


    for x in range(min1, max1, 1):
        xS = str(x)
        temp = []
        flag = False

        if not '0' in xS:

            for l in range(0,xS.__len__(),1):
                if xS.count(xS[l])>1:
                    flag=True

                else:

                    temp.append(xS[l])

            if flag==False:

                for y in range(min2,max2,1):
                    yS=str(y)
                    temp2 = []
                    flag = False

                    if x*y > max:
                        break

                    if not '0' in yS:

                        for l in range(0, yS.__len__(), 1):
                            if yS.count(yS[l]) > 1 or yS[l] in temp:
                                flag = True

                            else:

                                temp2.append(yS[l])

                        if flag==False:

                            prod = str(x*y)

                            if '0' in prod:
                                flag=True

                            else:
                                for z in range(0,prod.__len__(),1):
                                    if prod[z] in temp or prod[z] in temp2 or prod.count(prod[z])>1:
                                        flag=True

                            if flag ==False and not int(prod) in Results:
                                Results.append(int(prod))
                                print (x, y, prod)

                            flag = False

    return Results

Respuesta = Analysis(12,100,123,1000)

print (Respuesta, sum(Respuesta))

Respuesta = Analysis(1,10,1234,10000)

print (Respuesta, sum(Respuesta))