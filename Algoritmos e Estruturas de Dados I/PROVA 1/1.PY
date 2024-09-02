"""
Cada carro tem um desempenho, que é geralmente medido por quantos quilometros ele pode percorrer com 1 litro
de gasolina. Por exemplo, os carros mais econômicos podem fazer 16km/h. Escreve um programa em python que leia o
desempenho de um carro é um trajeto percorrido em um mês. Escrevea o quanto foi gasto em reais, considerando a gasolina R$ 5.85.
"""

desempenho = float(input('Qual o desempenho do carro em Km/l?: '))
trajeto_um_mes = float(input('Qual o trajeto percorrido em um mês? '))

preço_gasolina = 5.85
gasto = (trajeto_um_mes / desempenho) * preço_gasolina

print(f'O gasto do carro foi de R${gasto:.2f}')