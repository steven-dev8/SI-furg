"""Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor
e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Faça
um programa em Python que receba o nome do(a) ginasta, e as notas de sua
apresentação dadas pelos sete jurados. Ao final, informe a melhor nota, a pior nota e
a sua média final, conforme a descrição acima informada (ou seja, retirar a melhor e
a pior nota para calcular a média). As notas não são informadas em ordem (crescente
ou decrescente)."""

media = 0
count = 0

while count != 7:
    nota = int(input(f'Nota{count+1}: '))
    
    if count == 0:
        maior_nota = nota
        menor_nota = nota
    else:
        if nota > maior_nota:
            maior_nota = nota
        if nota < menor_nota:
            menor_nota = nota
    
    media = media + nota
    count = count + 1

media = (media - maior_nota - menor_nota) / 5
print(f'A maior nota foi {maior_nota}')
print(f'A menor nota foi {menor_nota}')
print(f'A media das notas foi {media:.2f}')