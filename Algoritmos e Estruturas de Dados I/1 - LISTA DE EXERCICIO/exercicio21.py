from random import randint

sorte = 0
sorteado = randint(1,1000000)

while sorte != sorteado:
    sorte = int(input('Adivinhe o número: '))

    if sorte > sorteado:
        print('Você errou. É UM NÚMERO MENOR')
    if sorte < sorteado:
        print('Você errou. É UM NÚMERO MAIOR')

print(f'Parabéns você acertou o número!!! O número é {sorteado}')