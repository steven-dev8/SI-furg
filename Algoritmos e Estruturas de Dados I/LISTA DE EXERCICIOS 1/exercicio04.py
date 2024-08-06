nota_check = freq_check = 0
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
nota4 = float(input('Quarta nota: '))
frequencia = int(input('Qual a porcentagem de frequência: '))

if frequencia >= 75:
    freq_check += 1
nota_total = (nota1 + nota2 + nota3 + nota4) / 4

if (nota1 <= 10 and nota1 >= 0) and (nota2 <= 10 and nota2 >= 0) and (nota3 <= 10 and nota3 >= 0) and (nota4 <= 10 and nota4 >= 0):
    if freq_check == 1:
        if nota_total >= 7 and freq_check == 1:
            print('Aprovado em Algoritimo e Estrutura de Dados I')
        if nota_total > 3 and nota_total < 7 and freq_check == 1:
            print('O aluno deverá fazer o EXAME em Algoritimo e Estrutura de Dados I')
        else:
            print('Reprovado em Algoritimo e Estrutura de Dados I')
    else:
        print('Reprovado em Algoritimo e Estrutura de Dados I')
else:
    print('Digite uma nota entre 0-10 ')