tijolo = input('Bloco: ')
qnt_blocos = int(input('Qnt: '))

count = 0
qnt_tijolo = tijolo
qnt_vezes = qnt_blocos

while count < qnt_vezes:
    espaço = ''
    deslocamento = 1

    while deslocamento < qnt_blocos:
        espaço = espaço + ' '
        deslocamento = deslocamento + 1

    print(f'{espaço}{qnt_tijolo}')

    qnt_tijolo = qnt_tijolo + tijolo + tijolo
    count = count + 1
    qnt_blocos = qnt_blocos - 1