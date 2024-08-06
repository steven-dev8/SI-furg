x = 0
y = 0
primo = 0

while x >= y and (x <= 0 and y <= 0):
    x = int(input('X: '))
    y = int(input('Y: '))

for cont in range(x , y + 1):
    for cont_primo in range(1, cont + 1):
        if cont % cont_primo == 0:
            primo = primo + 1

    if primo == 2:
            print(cont, end=' - ')

    primo = 0