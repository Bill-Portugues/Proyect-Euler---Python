
import time

def tester (h,a,b):
    if a ** 2 + b ** 2 == h ** 2 :
        flag = True

    else:
        flag=False

    return flag


def guess(trial):

    max = 0
    qmax = 0

    for z in range(1,trial,1):
        aux = 0



        for h in range(round(z / 3 + 1), z-2):

            for a in range(round((z - h)/2 + 1),h,1):

                if z - h - a  < 1:
                    break

                b =z -h-a

                if tester(h,a,b) == True:
                    #print (a,b,h, "-",z,"-")

                    aux+=1

        if aux>qmax:
            qmax = aux
            max=z

    return (max, qmax)


start = time.time()

print (guess(1000))


end = time.time()
print(end - start)

