"""Escreva um programa que leia dois valores x e y. Em seguida escreva quais são os
números primos contidos neste intervalo. Por exemplo, para x=3 e y=14 escreva:
3,5,7,11,13. Verifique se o usuário digitou x e y de modo que x<y."""

#Bloco de variáveis iniciais
x = 0
y = 0
qnt_divisor = 0
divisor = 2

while x >= y and (x <= 0 and y <= 0): #Faz testes até que X seja menor que Y e ambos seja maior que zero
    x = int(input('X: '))
    y = int(input('Y: '))

print(f'Os números primos entre {x} e {y} são: ') #Imprime os valores X e Y

while x <= y: #Enquanto X for menor ou igual a Y, o loop rodará
    while divisor <= 10: #Enquanto divisor for menor ou igual a 10
        if x % divisor == 0: #Se X dividido por "divisor" tiver resto = 0
            qnt_divisor += 1 #qnt_divisor vai receber +1, a cada vez que um número tiver um divisor com resto 0
        divisor += 1
        
    if qnt_divisor == 1 or qnt_divisor == 0: #Se qnt_divisor for igual a 1 ou 0, imprime o valor X
        print(x, end='')

    #Bloco de váriaveis de reset
    x += 1 #X agora virará o seu sucessor, Ex: X era 1 agora ele será 2
    qnt_divisor = 0
    divisor = 2