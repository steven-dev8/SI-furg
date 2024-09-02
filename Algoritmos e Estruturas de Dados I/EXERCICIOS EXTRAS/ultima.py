VERIFY = True

while VERIFY:    
    numero = int(input('Número: '))

    if numero > 0:
        VERIFY = False
    else:
        print('Digite um número positivo/inteiro e acima de 0')

while VERIFY == False:
    numero = numero / 2      

    if numero >= 1:
        print(f'Resultado da divisão {numero}')
    else:
        print('Chegou a zero!')
        VERIFY = True
