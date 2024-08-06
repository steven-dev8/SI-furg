number = int(input('Número: '))
fatorial = 1
less = number

print('5! = ', end='')

while less > 0:
    print(less, end=' x ')
    fatorial = fatorial * less
    less = less - 1

print(f'= {fatorial}')