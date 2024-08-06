nota1 = float(input('Nota1: '))
nota2 = float(input('Nota2: '))
nota3 = float(input('Nota3: '))
nota4 = float(input('Nota4: '))
nota5 = float(input('Nota5: '))
nota6 = float(input('Nota6: '))
nota7 = float(input('Nota7: '))

if nota1 > nota2 and nota1 > nota3 and nota1 > nota4 and nota1 > nota5 and nota1 > nota6 and nota1 > nota7:
    if nota2 < nota3 and nota2 < nota4 and nota2 < nota5 and nota2 < nota6 and nota2 < nota7:
        nota_maior = nota1
        nota_menor = nota2
    else:
        if nota3 < nota4 and nota3 < nota5 and nota3 < nota6 and nota3 < nota7:
            nota_maior = nota1
            nota_menor = nota3
        else:
            if nota4 < nota5 and nota4 < nota6 and nota4 < nota7:
                nota_maior = nota1
                nota_menor = nota4
            else:
                if nota5 < nota6 and nota5 < nota7:
                    nota_maior = nota1
                    nota_menor = nota5
                else:
                    if nota6 < nota7:
                        nota_maior = nota1
                        nota_menor = nota6
                    else:
                        nota_maior = nota1
                        nota_menor = nota7

if nota2 > nota1 and nota2 > nota3 and nota2 > nota4 and nota2 > nota5 and nota2 > nota6 and nota2 > nota7:
    if nota1 < nota3 and nota1 < nota4 and nota1 < nota5 and nota1 < nota6 and nota1 < nota7:
        nota_maior = nota2
        nota_menor = nota1
    else:
        if nota3 < nota4 and nota3 < nota5 and nota3 < nota6 and nota3 < nota7:
            nota_maior = nota2
            nota_menor = nota3
        else:
            if nota4 < nota5 and nota4 < nota6 and nota4 < nota7:
                nota_maior = nota2
                nota_menor = nota4
            else:
                if nota5 < nota6 and nota5 < nota7:
                    nota_maior = nota2
                    nota_menor = nota5
                else:
                    if nota6 < nota7:
                        nota_maior = nota2
                        nota_menor = nota6
                    else:
                        nota_maior = nota2
                        nota_menor = nota7

if nota3 > nota1 and nota3 > nota2 and nota3 > nota4 and nota3 > nota5 and nota3 > nota6 and nota3 > nota7:
    if nota1 < nota2 and nota1 < nota4 and nota1 < nota5 and nota1 < nota6 and nota1 < nota7:
        nota_maior = nota3
        nota_menor = nota1
    else:
        if nota2 < nota4 and nota2 < nota5 and nota2 < nota6 and nota2 < nota7:
            nota_maior = nota3
            nota_menor = nota2
        else:
            if nota4 < nota5 and nota4 < nota6 and nota4 < nota7:
                nota_maior = nota3
                nota_menor = nota4
            else:
                if nota5 < nota6 and nota5 < nota7:
                    nota_maior = nota3
                    nota_menor = nota5
                else:
                    if nota6 < nota7:
                        nota_maior = nota3
                        nota_menor = nota6
                    else:
                        nota_maior = nota3
                        nota_menor = nota7

if nota4 > nota1 and nota4 > nota2 and nota4 > nota3 and nota4 > nota5 and nota4 > nota6 and nota4 > nota7:
    if nota1 < nota2 and nota1 < nota3 and nota1 < nota5 and nota1 < nota6 and nota1 < nota7:
        nota_maior = nota4
        nota_menor = nota1
    else:
        if nota2 < nota3 and nota2 < nota5 and nota2 < nota6 and nota2 < nota7:
            nota_maior = nota4
            nota_menor = nota2
        else:
            if nota3 < nota5 and nota3 < nota6 and nota3 < nota7:
                nota_maior = nota4
                nota_menor = nota3
            else:
                if nota5 < nota6 and nota5 < nota7:
                    nota_maior = nota4
                    nota_menor = nota5
                else:
                    if nota6 < nota7:
                        nota_maior = nota4
                        nota_menor = nota6
                    else:
                        nota_maior = nota4
                        nota_menor = nota7

if nota5 > nota1 and nota5 > nota2 and nota5 > nota3 and nota5 > nota4 and nota5 > nota6 and nota5 > nota7:
    if nota1 < nota2 and nota1 < nota3 and nota1 < nota4 and nota1 < nota6 and nota1 < nota7:
        nota_maior = nota5
        nota_menor = nota1
    else:
        if nota2 < nota3 and nota2 < nota4 and nota2 < nota6 and nota2 < nota7:
            nota_maior = nota5
            nota_menor = nota2
        else:
            if nota3 < nota4 and nota3 < nota6 and nota3 < nota7:
                nota_maior = nota5
                nota_menor = nota3
            else:
                if nota4 < nota6 and nota4 < nota7:
                    nota_maior = nota5
                    nota_menor = nota4
                else:
                    if nota6 < nota7:
                        nota_maior = nota5
                        nota_menor = nota6
                    else:
                        nota_maior = nota5
                        nota_menor = nota7

if nota6 > nota1 and nota6 > nota2 and nota6 > nota3 and nota6 > nota4 and nota6 > nota5 and nota6 > nota7:
    if nota1 < nota2 and nota1 < nota3 and nota1 < nota4 and nota1 < nota5 and nota1 < nota7:
        nota_maior = nota6
        nota_menor = nota1
    else:
        if nota2 < nota3 and nota2 < nota4 and nota2 < nota5 and nota2 < nota7:
            nota_maior = nota6
            nota_menor = nota2
        else:
            if nota3 < nota4 and nota3 < nota5 and nota3 < nota7:
                nota_maior = nota6
                nota_menor = nota3
            else:
                if nota4 < nota5 and nota4 < nota7:
                    nota_maior = nota6
                    nota_menor = nota4
                else:
                    if nota5 < nota7:
                        nota_maior = nota6
                        nota_menor = nota5
                    else:
                        nota_maior = nota6
                        nota_menor = nota7

if nota7 > nota1 and nota7 > nota2 and nota7 > nota3 and nota7 > nota4 and nota7 > nota5 and nota7 > nota6:
    if nota1 < nota2 and nota1 < nota3 and nota1 < nota4 and nota1 < nota5 and nota1 < nota6:
        nota_maior = nota7
        nota_menor = nota1
    else:
        if nota2 < nota3 and nota2 < nota4 and nota2 < nota5 and nota2 < nota6:
            nota_maior = nota7
            nota_menor = nota2
        else:
            if nota3 < nota4 and nota3 < nota5 and nota3 < nota6:
                nota_maior = nota7
                nota_menor = nota3
            else:
                if nota4 < nota5 and nota4 < nota6:
                    nota_maior = nota7
                    nota_menor = nota4
                else:
                    if nota5 < nota6:
                        nota_maior = nota7
                        nota_menor = nota5
                    else:
                        nota_maior = nota7
                        nota_menor = nota6

media = (nota1 + nota2 + nota3 + nota4 + nota5 + nota6 + nota7 - nota_maior - nota_menor) / 5

print(f'A maior nota: {nota_maior:.2f}, a menor: {nota_menor:.2f} e a média: {media:.2f}')