

def Factorial_digit_sum(number):

    overall =1
    overall2=0
    for x in range(number,0,-1):
        overall *= x

    for y in range(0,len(str(overall)),1):
        overall2 +=int(str(overall)[y])

    return overall2

print(Factorial_digit_sum(100))