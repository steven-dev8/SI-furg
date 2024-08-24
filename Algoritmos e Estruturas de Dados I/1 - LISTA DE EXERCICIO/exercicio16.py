c = 1
check = 0
number = 0

while number <= 0:
    number = int(input('Número: '))

while c <= number:
    if number % c == 0:
        check = check + 1
    c = c + 1
if check == 2:
    print(f'O número {number} é primo.')
else:
    print(f'O número {number} não é primo.')