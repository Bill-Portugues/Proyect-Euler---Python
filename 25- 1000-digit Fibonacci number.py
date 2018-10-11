
def fibonacci():

    index=2
    FN2 = 1
    FN1 = 1
    FN=0

    while (str(FN).__len__() < 1000):

        index += 1
        FN = FN1+FN2
        FN2=FN1
        FN1=FN

    print(index, "NUMERO: ", FN)

    return index


print (fibonacci())