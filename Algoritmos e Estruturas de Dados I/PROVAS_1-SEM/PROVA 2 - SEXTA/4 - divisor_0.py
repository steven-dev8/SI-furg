number = int(input('Digite um número inteiro: '))
divisor = number

print(f'Os divisores de {number} são: ', end='')
while divisor > 0:
    if number % divisor == 0:
        print(f'{divisor}', end=' ')
    divisor -= 1