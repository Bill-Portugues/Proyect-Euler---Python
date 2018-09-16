
def tester (a,b,c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    else:
        return False


def guess(trial):


    end = "NO"
    limiteC = round(trial / 3 + 1)
    limiteB = round((trial - limiteC)/2 +1)
    for c in range(limiteC, trial):
        for b in range(round((trial - limiteC)/2),trial-c,1):
            a=trial-c-b
            if ((a + b +c) != trial or not a<b<c ):
                break

            if tester(a,b,c) == True:
                print (a,b,c)
                print (a * b * c)
                end = "OK"
                break
        if end == "OK":
            break

guess(1000)