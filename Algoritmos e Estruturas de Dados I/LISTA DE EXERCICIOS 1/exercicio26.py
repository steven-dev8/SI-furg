from time import sleep

minuto = 0
segundo1 = 0
segundo2 = 0

while minuto != 10:
    if segundo2 == 10:
        segundo1 = segundo1 + 1
        segundo2 = 0
    if segundo1 == 6:
        minuto = minuto + 1
        segundo1 = 0
    print(f'{minuto}:{segundo1}{segundo2}')
    sleep(1)
    segundo2 = segundo2 + 1