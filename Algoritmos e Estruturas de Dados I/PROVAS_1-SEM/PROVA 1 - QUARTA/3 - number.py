VERIFY = True

while VERIFY:
    numero = int(input('Digite um número entre (1000-9999): '))
    
    if numero >= 1000 and numero <= 9999:
        VERIFY = False

a = (numero // 1000)
resto_a = numero % 1000

b = (resto_a // 100)
resto_b = numero % 100

c = (resto_b // 10)
resto_c = numero % 10

d = (resto_c % 10)

print(f'{d}{c}{b}{a}')

