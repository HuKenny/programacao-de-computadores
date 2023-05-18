time1_gols=int(input('Digite quantos gols o time1 fez:'))
time2_gols=int(input('Digite quantos gols o time2 fez:'))

if time1_gols == time2_gols:
    print('O jogo empatou!')
elif time1_gols >= time2_gols:
    print('O time1 ganhou!')
else:
    print('o time2 ganhou!')