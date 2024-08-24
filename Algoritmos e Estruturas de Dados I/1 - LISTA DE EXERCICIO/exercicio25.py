number = 10

while number < 100:
    if number >= 10:

        if number >= 10 and number < 30:
            if number % 3 == 0:
                print(number)
            number = number + 1

        if number % 10 == 0 and number >= 30:
            if (number + 1) % 3 == 0:
                print(number + 1)
            if (number + 2) % 3 == 0:
                print(number + 2)
            number = number + 10