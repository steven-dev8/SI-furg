"""
Crie um programa que calcule a raiz quadrada de "n", sem usar a biblioteca math,
sem usar potência e não pode fazer os loops/testes apenas com adição de 0.00001
"""

n = int(input('Número: '))#Da entrada de um número
div = n#A variável div vai receber o n
r = div * div#A variável r vai receber div * div

while r > n: #Enquanto div * div for maior que o n
    div = div / 2 #div vai receber o valor dele mesmo dividido por 2
    r = div * div #r vai receber o valor de div * div, nessa parte div já ta com seu valor reduzido, pois foi dividido pela metade

while r < n:#Enquanto r for menor que n
    div = div + 0.00001#div vai receber o seu número + 0.00001
    r = div * div#r vai receber o valor de div * div, nessa parte div já ta com seu valor somado com 0.00001

print(f"{div:.4f}")#Imprime o valor de "div", que é a raiz quadrada de "n"