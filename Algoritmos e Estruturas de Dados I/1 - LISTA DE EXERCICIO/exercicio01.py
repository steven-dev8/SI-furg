"""Faça um programa que, ao receber os valores da largura e do comprimento de uma
figura geométrica, mostre se esta é um quadrado ou apenas um retângulo. Caso um
valor seja menor ou igual a zero, deve-se mostrar um erro."""

#Da entrada do valor dos lados
first_value = int(input(': '))
second_value = int(input(': '))

if first_value == second_value: #Verifica se os lados são iguais
    print('A square') #Se a condição for verdadeira, imprime "Um quadrado"
else: 
    print('A rectangle') #Caso o contrário, se for falsa imprime "Um retângulo"

if first_value <= 0 or second_value <= 0: #Verifica se os valores dos lados são menor ou igual a 0
    print('ERROR') #Se a condição for verdadeira, imprime "ERROR"
    