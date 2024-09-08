result = 0
VALID = True

while VALID:
    numero = int(input('Digite um número inteiro: '))
    if numero > 0:
        VALID = False
    else:
        print('ERRO, digite um numero inteiro positivo.')

i = 1
result = numero
soma = 0

while result != 0:
    result = (numero // 10 ** i)
    i += 1

i -= 1
c = 0

while i != -1:
    if c == 0:
        potencia = (numero // 10 ** i)
        resto = numero % (10 ** i) 
        c += 1
    else:
        potencia = (resto // 10 ** i)
        resto = numero % (10 ** i) 
    
    soma += potencia

    i -= 1
print(f'A soma de cada dígito é {soma}')