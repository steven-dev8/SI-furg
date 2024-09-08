VERIFY = True
print('Calculando a área de uma retângulo')

while VERIFY:
    altura = float(input('Digite a altura: '))
    largura = float(input('Digite a largura: '))

    if altura != largura and altura > 0 and largura > 0:
        VERIFY = False
    else:
        print('Digite valores válidos.')

area = altura * largura

print(f'A área de {altura}x{largura} é {area}m²')