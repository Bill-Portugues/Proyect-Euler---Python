def findlargest (max):

    maximo =[[0,0]]

    for y in range (max,1,-1):
        counter = 0
        x = y
        while x != 1:

            if x % 2 == 0:
                x = x / 2

            else:
                x = x * 3 +1

            counter +=1

        if counter > maximo[0][1]:
            maximo[0] = y,counter
            print ('Nuevo maximo %d %d' %(y,counter))
          #  maximo[0][1] = counter


findlargest(999999)
