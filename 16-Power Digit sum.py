



def power_digit_sum(number,power):

    resultado=0

    number = number ** power

    number_str = str(number)

    for x in range(0, len(number_str), 1):

        resultado += int(number_str[x])

    print (resultado)


power_digit_sum(2,1000)

