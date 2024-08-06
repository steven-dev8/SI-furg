number = int(input('Número: '))
fatorial = number
less = number

print(f'5!', end=' = ')

while less != 1:
    print(less, end=' x ')
    less = less - 1
    result = fatorial * less
    fatorial = result
    
print(f'1 = {result}')