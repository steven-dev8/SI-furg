cont = 0
numb = int(input('Número: '))

print('Ímpares: ', end='')

if numb % 2 == 0:
    numb = numb + 1
    
    while cont != 6:
        cont = cont + 1
        print(numb, end=' - ' if cont != 6 else '')
        numb = numb + 2
        

while cont != 6:
    cont = cont + 1
    print(numb, end=' - ' if cont != 6 else '')
    numb = numb + 2 