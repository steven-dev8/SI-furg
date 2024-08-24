nome = 'julia de martin mendes de sá'
new_string = ''
i = 0
j = 0

while i < len(nome):
    a = ord(nome[i])

    if j == 0:
        b = chr(a - 32)
        new_string += b
        j += 1

    else:
        new_string += nome[i]
    
    if a == 32:
        j = 0

    i += 1
print(new_string)