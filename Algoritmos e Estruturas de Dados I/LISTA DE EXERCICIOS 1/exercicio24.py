"""Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor
e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Faça
um programa em Python que receba o nome do(a) ginasta, e as notas de sua
apresentação dadas pelos sete jurados. Ao final, informe a melhor nota, a pior nota e
a sua média final, conforme a descrição acima informada (ou seja, retirar a melhor e
a pior nota para calcular a média). As notas não são informadas em ordem (crescente
ou decrescente)."""

#Bloco de entradas
nota1 = float(input('Nota1: ')) #Da input das notas de 1 a 7
#As váriaveis nota_maior e nota_menor vai receber o valor de nota1
nota_maior = nota1 
nota_menor = nota1

nota2 = float(input('Nota2: '))
if nota_maior < nota2:#Se nota_maior for menor que nota2, então nota_maior receberá o valor de nota2
    nota_maior = nota2
if nota_menor > nota2:#Se nota_menor for menor que nota2, então nota_menor receberá o valor de nota2
    nota_menor = nota2

#Segue a sentença aplicando o bloco de condicionais da nota3 até a nota7
nota3 = float(input('Nota3: '))
if nota_maior < nota3:
    nota_maior = nota3
if nota_menor > nota3:
    nota_menor = nota3

nota4 = float(input('Nota4: '))
if nota_maior < nota4:
    nota_maior = nota4
if nota_menor > nota4:
    nota_menor = nota4

nota5 = float(input('Nota5: '))
if nota_maior < nota5:
    nota_maior = nota5
if nota_menor > nota5:
    nota_menor = nota5

nota6 = float(input('Nota6: '))
if nota_maior < nota6:
    nota_maior = nota6
if nota_menor > nota6:
    nota_menor = nota6

nota7 = float(input('Nota7: '))
if nota_maior < nota7:
    nota_maior = nota7
if nota_menor > nota7:
    nota_menor = nota7

#media = Soma as médias e subtrai a maior nota e a menor, depois divide por 5
media = (nota1 + nota2 + nota3 + nota4 + nota5 + nota6 + nota7 - nota_maior - nota_menor) / 5

#Imprime a maior nota, a menor e a média
print(f'Maior nota: {nota_maior} \nMenor nota: {nota_menor} \nMédia: {media} ')
