nome = input('digite um nome: ')
new_string = ''
i = 0 

while i < len(nome):
    a = ord(nome[i])
    
    if a == 32:
        new_string += chr(32)
    else:
        b = a + 32
        new_string += chr(b)
    i += 1

print(new_string)