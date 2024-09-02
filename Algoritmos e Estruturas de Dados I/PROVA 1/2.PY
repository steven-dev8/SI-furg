CHECK = True
VALID = True

DATA = input('Digite uma data (DD/MM/AAAA) entre 2024-2025: ')
    
while CHECK:
    if (DATA[2] == '/' and DATA[5] == '/'):
        DIA = int(DATA[0:2])
        MES = int(DATA[3:5])
        ANO = int(DATA[6:10])

        if ANO < 2024 or ANO > 2025:
            DATA = input('DATA INVALIDA!!!. Digite uma data (DD/MM/AAAA) entre 2024-2025: ')
        else:
            VALID = False
    else:
        DATA = input('FORMATO DE DATA INVALIDO!!!. Digite uma data (DD/MM/AAAA) entre 2024-2025: ')

    if VALID == False and ANO == 2024:
        if MES == 2 and (DIA < 1 or DIA > 29):
            DATA = input('DATA INVALIDA!!!. Digite uma data (DD/MM/AAAA) entre 2024-2025: ')
        elif (MES == 1 or MES == 3 or MES == 5 or MES == 7 or MES == 8 or MES == 10 or MES == 12) and (DIA < 1 or DIA > 31):
            DATA = input('DATA INVALIDA!!!. Digite uma data (DD/MM/AAAA) entre 2024-2025: ')
        elif (MES == 4 or MES == 6 or MES == 9 or MES == 11) and (DIA < 1 or DIA > 30):
            DATA = input('DATA INVALIDA!!!. Digite uma data (DD/MM/AAAA) entre 2024-2025: ')
        elif MES > 12 or MES < 1:
            DATA = input('DATA INVALIDA!!!. Digite uma data (DD/MM/AAAA) entre 2024-2025: ')
        else:
            CHECK = False
    elif VALID == False and ANO == 2025:
        if MES == 2 and (DIA < 1 or DIA > 28):
            DATA = input('DATA INVALIDA!!!. Digite uma data (DD/MM/AAAA) entre 2024-2025: ')
        elif (MES == 1 or MES == 3 or MES == 5 or MES == 7 or MES == 8 or MES == 10 or MES == 12) and (DIA < 1 or DIA > 31):
            DATA = input('DATA INVALIDA!!!. Digite uma data (DD/MM/AAAA) entre 2024-2025: ')
        elif (MES == 4 or MES == 6 or MES == 9 or MES == 11) and (DIA < 1 or DIA > 30):
            DATA = input('DATA INVALIDA!!!. Digite uma data (DD/MM/AAAA) entre 2024-2025: ')
        elif MES > 12 or MES < 1:
            DATA = input('DATA INVALIDA!!!. Digite uma data (DD/MM/AAAA) entre 2024-2025: ')
        else:
            CHECK = False


DIA_1 = 1
MES_1 = 1
ANO_1 = 2024

I = 0


while DIA_1 != DIA or MES_1 != MES or ANO_1 != ANO:
    
    DIA_1 += 1
    I += 1

    if ANO_1 == 2024:
        if MES_1 == 2 and DIA_1 > 29:
            MES_1 += 1
            DIA_1 = 1
        elif (MES_1 == 1 or MES_1 == 3 or MES_1 == 5 or MES_1 == 7 or MES_1 == 8 or MES_1 == 10) and DIA_1 > 31:
            MES_1 += 1
            DIA_1 = 1
        elif (MES_1 == 4 or MES_1 == 6 or MES_1 == 9 or MES_1 == 11) and DIA_1 > 30:
            MES_1 += 1
            DIA_1 = 1
        elif MES_1 == 12 and DIA_1 > 31:
            MES_1 = 1
            DIA_1 = 1
            ANO_1 += 1

    elif ANO_1 == 2025:
        if MES_1 == 2 and DIA_1 > 28:
            MES_1 += 1
            DIA_1 = 1
        elif (MES_1 == 1 or MES_1 == 3 or MES_1 == 5 or MES_1 == 7 or MES_1 == 8 or MES_1 == 10) and DIA_1 > 31:
            MES_1 += 1
            DIA_1 = 1
        elif (MES_1 == 4 or MES_1 == 6 or MES_1 == 9 or MES_1 == 11) and DIA_1 > 30:
            MES_1 += 1
            DIA_1 = 1
        elif MES_1 == 12 and DIA_1 > 31:
            MES_1 = 1
            DIA_1 = 1
I += 1

DIA_SEMANA = I % 7

if DIA_SEMANA == 1:
    print('É uma segunda-feira')
if DIA_SEMANA == 2:
    print('É uma terça-feira')
if DIA_SEMANA == 3:
    print('É uma quarta-feira')
if DIA_SEMANA == 4:
    print('É uma quinta-feira')
if DIA_SEMANA == 5:
    print('É uma sexta-feira')
if DIA_SEMANA == 6:
    print('É um sabado')
if DIA_SEMANA == 0:
    print('É um domingo')
    