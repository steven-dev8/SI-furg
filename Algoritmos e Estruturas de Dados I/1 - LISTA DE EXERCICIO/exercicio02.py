viagem_quest = input('A viagem custará menos de R$ 30? [S/N] ').upper()[0]
wifi_quest =  input('Terá Wifi? [S/N] ').upper()[0]
piscina_quest = input('Terá piscina? [S/N] ').upper()[0]
churras_quest = input('Terá churrasqueira? [S/N]').upper()[0]

if 'S' in viagem_quest:
    if 'S' in wifi_quest:
        if 'S' in piscina_quest:
            print('A VIAGEM OCORRERÁ')
        else:
            if 'S' in churras_quest:
                print('A VIAGEM OCORRERÁ')
            else:
                print('A VIAGEM NÃO OCORRERÁ')
    else:
        if 'S' in piscina_quest:
            if 'S' in churras_quest:
                print('A VIAGEM OCORRERÁ')
            else:
                print('A VIAGEM NÃO OCORRERÁ')
        else:
            print('A VIAGEM NÃO OCORRERÁ')
else:
    print('A VIAGEM NÃO OCORRERÁ')