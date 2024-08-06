time1 = input('Time1: ')
time2 = input('Time2: ') 
time3 = input('Time3: ')
time4 = input('Time4: ')
print('-='*20)
p1_1 = int(input(f'Gols 1 partida [{time1}]: '))
p1_2 = int(input(f'Gols 1 partida [{time2}]: '))
print('-='*20)
p2_1 = int(input(f'Gols 2 partida [{time3}]: '))
p2_2 = int(input(f'Gols 2 partida [{time4}]: '))
if p1_1 > p1_2:
    time_pass1 = time1
else:
    time_pass1 = time2
if p2_1 > p2_2:
    time_pass2 = time3
else:
    time_pass2 = time4
print('-='*20)
print(f'3 partida entre {time_pass1} X {time_pass2}')
p3_1 = int(input(f'Gols 3 partida [{time_pass1}]: '))
p3_2 = int(input(f'Gols 3 partida [{time_pass2}]: '))
print('-='*20)
if p3_1 > p3_2:
    print(f'CAMPEÃO {time_pass1}')
else:
    print(f'CAMPEÃO {time_pass2}')