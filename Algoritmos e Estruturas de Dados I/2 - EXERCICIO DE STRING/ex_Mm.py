frase = 'JOAO vitor'
new_string = ''
i = 0

while i < len(frase):
    a = ord(frase[i])

    if a > 64 and a < 91:
        new_string += chr(a + 32)
    else:
        new_string += frase[i]

    i += 1
print(new_string)