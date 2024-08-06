addition = 1
first_value = 0
cont = 0

sequence = int(input('Termo: '))

while cont != sequence:
    cont = cont + 1
    result = first_value + addition
    print(first_value, end=' ')
    first_value = addition
    addition = result