text = input('Musica: ').upper()
vogal = str(input('Digite a vogal: ')).upper()[0]

new_text = ''
a = 0

while a != len(text):
    if text[a]=='A'or text[a]=='E'or text[a]=='I' or text[a]=='O' or text[a]=='U':
        new_text = new_text + vogal
    else:
        new_text = new_text + text[a]

    a = a + 1

print(new_text)