number = 1
cont = 0
store = 0

while number != 0:
    number = int(input('Número - 0 PARAR: '))
    store = store + number
    if number != 0:
        cont = cont + 1

print(f'Você digitou {cont} números e a media entre eles é {store/cont:.2f}')