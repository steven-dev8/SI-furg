mat = input('Material: ')
qnt = int(input('Quantidade: '))
cont = 1
space = qnt 

for c in range(1, qnt + 1):
    print(f' ' * space, mat * cont)
    cont = cont + 2
    space = space - 1