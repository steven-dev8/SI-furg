ano_pass = 0
dia = int(input('DIA: '))
mes = int(input('MES: '))
ano = int(input('ANO: '))
if ano % 100 == 0:
    if ano % 400 == 0:
        ano_text = 'o ano é bissexto'
        ano_pass = 1
    else:
        ano_text = 'o ano não é bissexto'
else:
    if ano % 4 == 0:
        ano_text = 'o ano é bissexto'
        ano_pass = 1
    else:
        ano_text = 'o ano não é bissexto'
if (mes > 0 and mes <= 12) and (dia <= 31 and dia > 0):
    if ano_pass == 1:
        if mes == 2:
            if dia <= 29:
                print(f'Data válida, {ano_text}')
            else:
                print('Data inválida.')
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia == 31:
                print('Digite uma data válida.')
            else:
                print(f'Data válida, {ano_text}')
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            print(f'Data válida, {ano_text}')
    if ano_pass == 0:
        if mes == 2:
            if dia <= 29:
                print('Data inválida')
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia == 31:
                print('Digite uma data válida.')
            else:
                print(f'Data válida, {ano_text}')
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            print(f'Data válida, {ano_text} ')
else:
    print('Insira uma data válida.')