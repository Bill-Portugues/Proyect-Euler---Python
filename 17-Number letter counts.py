

Written_numbers20 = ["","one","two","three","four","five","six","seven","eight","nine","ten",
                   "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen","twenty"]

List20_90 =	[0,0,6,6,5,5,5,7,6,6]


Counting_numbers20 = [len(x) for x in Written_numbers20[:]]

hundred_and = 10
hundred=7
thousand = 8


def number_letter_counts(number):

    overallSum=0

    for x in range(1,number+1,1):
        overallSum += letter_counting(str(x))

    print (overallSum)


def letter_counting(numb):

    overallSum=0

    largo=len(numb)

    while largo>0:

        num_cutter=1

        # 4 Digits
        if largo == 4:
            overallSum += Counting_numbers20[int(numb[:1])] + thousand

        # 3 Digits
        if largo == 3:
           if numb[1:]=="00":
               overallSum += Counting_numbers20[int(numb[:1])] + hundred
           else:
               overallSum += Counting_numbers20[int(numb[:1])] + hundred_and


        #Two Digits
        if largo == 2:

            #Special cases (1-20)
            if int(numb) <= 20:
                overallSum += Counting_numbers20[int(numb)]
                num_cutter = 2  # tremm two digits at one step

            else:
                overallSum += List20_90[int(numb[:1])]


        #Just One Digit
        if largo == 1:
           overallSum += Counting_numbers20[int(numb)]

        #print(numb, overallSum)

        numb = numb[num_cutter:]

        while numb[:1]=="0":
            numb = numb[1:]

        largo = len(numb)

 #   print (numb, overallSum)
    return overallSum

number_letter_counts(1000)
#letter_counting("226")
