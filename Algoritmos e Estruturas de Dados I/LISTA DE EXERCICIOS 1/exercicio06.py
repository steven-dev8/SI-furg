number_1 = int(input('N1: '))
number_2 = int(input('N2: '))
number_3 = int(input('N3: '))

if number_1 > number_2 and number_1 > number_3:
    if number_2 > number_3:
        print(number_3, number_2, number_1)
    else:
        print(number_2, number_3, number_1)

if number_2 > number_1 and number_2 > number_3:
    if number_3 > number_1:
        print(number_1, number_3, number_2)
    else:
        print(number_3, number_1, number_2)

if number_3 > number_1 and number_3 > number_2:
    if number_2 > number_1:
        print(number_1, number_2, number_3)
    else:
        print(number_2, number_1, number_3)
        
if number_1 == number_2 == number_3:
    print(number_1, number_2, number_3)