VERIFY = True

while VERIFY:
    numero = int(input('Digite um número entre (10-999): '))

    if numero >= 10 and numero <= 999:
        VERIFY = False