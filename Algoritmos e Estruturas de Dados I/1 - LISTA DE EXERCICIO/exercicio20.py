"""Escreva um programa que leia diversos funcionários e seu respectivo salario, ate que
o nome de um funcionário seja “fim”. Em seguida escreva:
a) O nome do funcionário com maior salário
b) O nome do funcionário com menor salário
c) A média dos salários digitados"""

soma_salario = 0
cont_salario = 0
c = 0
nome = ''

print('DIGITE "FIM" PARA TERMINAR O PROGRAMA')

while nome != "FIM":
    nome = input('Nome: ').upper() 

    if nome != 'FIM':
        salario = float(input('Salário: '))

        if c == 1:
            if salario > salario_maior:
                nome_maior = nome
                salario_maior = salario

            if salario < salario_menor:
                salario_menor = salario
                nome_menor = nome

            soma_salario = soma_salario + salario
            cont_salario = cont_salario + 1

        if c == 0:
            salario_maior = salario
            nome_maior = nome
            salario_menor = salario
            nome_menor = nome
            
            c = c + 1
            soma_salario = salario
            cont_salario = cont_salario + 1

media = soma_salario / cont_salario

print('-' * 35)
print(f'O MAIOR SALÁRIO É DE {nome_maior} COM R${salario_maior:.2f}')
print(f'O MENOR SALÁRIO É DE {nome_menor} COM R${salario_menor:.2f}')
print(f'A MÉDIA DO SALÁRIOS É DE R${media:.2f}')