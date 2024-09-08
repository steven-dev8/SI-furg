CHECK = True
VALID = True

DATA = input('Digite uma data (DD/MM/AAAA): ')
    
while CHECK:
    if DATA[2] == '/' and DATA[5] == '/':
        VALID = False
        DIA = int(DATA[0] + DATA[1])
        MES = int(DATA[3] + DATA[4])
        ANO = int(DATA[6:len(DATA)])
    else:
        DATA = input('FORMATO DE DATA INVALIDO!!!. Digite uma data (DD/MM/AAAA): ')

    if VALID == False:
        if MES == 2 and (DIA < 1 or DIA > 28):
            DATA = input('DATA INVALIDA!!!. Digite uma data (DD/MM/AAAA): ')
        elif (MES == 1 or MES == 3 or MES == 5 or MES == 7 or MES == 8 or MES == 10 or MES == 12) and (DIA < 1 or DIA > 31):
            DATA = input('DATA INVALIDA!!!. Digite uma data (DD/MM/AAAA): ')
        elif (MES == 4 or MES == 6 or MES == 9 or MES == 11) and (DIA < 1 or DIA > 30):
            DATA = input('DATA INVALIDA!!!. Digite uma data (DD/MM/AAAA): ')
        elif MES > 12 or MES < 1:
            DATA = input('DATA INVALIDA!!!. Digite uma data (DD/MM/AAAA): ')
        else:
            CHECK = False

DIAS_MAIS = int(input('Dias a mais: '))

I = 0

while I != DIAS_MAIS:
    DIA += 1

    if MES == 2 and DIA > 28:
        MES += 1
        DIA = 1
    if (MES == 1 or MES == 3 or MES == 5 or MES == 7 or MES == 8 or MES == 10) and DIA > 31:
        MES += 1
        DIA = 1
    if (MES == 4 or MES == 6 or MES == 9 or MES == 11) and DIA > 30:
        MES += 1
        DIA = 1
    if MES == 12 and DIA > 31:
        MES = 1
        DIA = 1
        ANO += 1

    I += 1

print(f'{DIA}/{MES}/{ANO}')