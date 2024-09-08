desempenho = float(input('Qual o desempenho do carro em Km/l?: '))
trajeto_um_mes = float(input('Qual o trajeto percorrido em um mês? '))

preço_gasolina = 5.85
gasto = (trajeto_um_mes / desempenho) * preço_gasolina

print(f'O gasto do carro foi de R${gasto:.2f}')