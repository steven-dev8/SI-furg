a = int(input('Lado A: '))
b = int(input('Lado B: '))
c = int(input('Lado C: '))

if a > 0 and b > 0 and c > 0:
    if a + b >= c and a + c >= b and b + c >= a:
        if a == b == c:
            print('TRIÂNGULO EQUILÁTERO')
        else:
            if a == b != c or a == c != b or b == c != a:
                print('TRIÂNGULO ISÓSCELES')
            else:
                print('TRIANGULO ESCALENO')
    else:
        print('NÃO É UM TRIÂNGULO')
else:
    print('TRIÂNGULO INVÁLIDO')