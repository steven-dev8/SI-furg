salario = int(input('Digite a renda mensal: '))
tabela = int(input('SELECIONE UMA DAS OPÇÕES ABAIXO\n'
                   '1 - SEM CORREÇÃO\n'
                   '2 - COM CORREÇÃO DAS PERDAS NO GOVERNO BOLSONSARO\n'
                   '3 - COM CORREÇÃO INTEGRAL\n'
                   ': '))
if tabela == 1:
    if salario <= 1903.98:
        print('Insento do imposto de renda')
    if salario > 1903.98 and salario <= 2826.65:
        salario_imposto = (salario * 7.50) / 100
        imposto_ano = (salario_imposto - 142.80) * 12
        print(f'Imposto de renda de 7,5% sobre R${salario}, pagará ao ano R${imposto_ano:.2f} de imposto.')
    if salario > 2826.65 and salario <= 3751.05:
        salario_imposto = (salario * 15) / 100
        imposto_ano = (salario_imposto - 354.80) * 12
        print(f'Imposto de renda de 15% sobre R${salario}, pagará ao ano R${imposto_ano:.2f} de imposto.')
    if salario > 3751.05 and salario <= 4664.68:
        salario_imposto = (salario * 22.50) / 100
        imposto_ano = (salario_imposto - 636.13) * 12
        print(f'Imposto de renda de 22.50% sobre R${salario}, pagará ao ano R${imposto_ano:.2f} de imposto.')
    if salario > 4664.68:
        salario_imposto = (salario * 27.50) / 100
        imposto_ano = (salario_imposto - 869.36) * 12
        print(f'Imposto de renda de 27.50% sobre R${salario}, pagará ao ano R${imposto_ano:.2f} de imposto.')

if tabela == 2:
    if salario <= 2500.44:
        print('Insento do imposto de renda')
    if salario > 2500.44 and salario <= 3712.16:
        salario_imposto = (salario * 7.50) / 100
        imposto_ano = (salario_imposto - 187.54) * 12
        print(f'Imposto de renda de 7,5% sobre R${salario}, pagará ao ano R${imposto_ano:.2f} de imposto.')
    if salario > 3712.16 and salario <= 4926.14:
        salario_imposto = (salario * 15) / 100
        imposto_ano = (salario_imposto - 465.95) * 12
        print(f'Imposto de renda de 15% sobre R${salario}, pagará ao ano R${imposto_ano:.2f} de imposto.')
    if salario > 4926.14 and salario <= 6125.99:
        salario_imposto = (salario * 22.50) / 100
        imposto_ano = (salario_imposto - 835.41) * 12
        print(f'Imposto de renda de 22.50% sobre R${salario}, pagará ao ano R${imposto_ano:.2f} de imposto.')
    if salario > 6125.99:
        salario_imposto = (salario * 27.50) / 100
        imposto_ano = (salario_imposto - 1141.71) * 12
        print(f'Imposto de renda de 27.50% sobre R${salario}, pagará ao ano R${imposto_ano:.2f} de imposto.')

if tabela == 3:
    if salario <= 4710.49:
        print('Insento do imposto de renda')
    if salario > 4710.49 and salario <= 6993.20:
        salario_imposto = (salario * 7.50) / 100
        imposto_ano = (salario_imposto - 353.29) * 12
        print(f'Imposto de renda de 7,5% sobre R${salario}, pagará ao ano R${imposto_ano:.2f} de imposto.')
    if salario > 6993.20 and salario <= 9280.19:
        salario_imposto = (salario * 15) / 100
        imposto_ano = (salario_imposto - 877.78) * 12
        print(f'Imposto de renda de 15% sobre R${salario}, pagará ao ano R${imposto_ano:.2f} de imposto.')
    if salario > 9280.19 and salario <= 11540.53:
        salario_imposto = (salario * 22.50) / 100
        imposto_ano = (salario_imposto - 1573.80) * 12
        print(f'Imposto de renda de 22.50% sobre R${salario}, pagará ao ano R${imposto_ano:.2f} de imposto.')
    if salario > 11540.53:
        salario_imposto = (salario * 27.50) / 100
        imposto_ano = (salario_imposto - 2150.82) * 12
        print(f'Imposto de renda de 27.50% sobre R${salario}, pagará ao ano R${imposto_ano:.2f} de imposto.')
        
if tabela < 1 or tabela > 3:
    print('OPÇÃO INVÁLIDA')