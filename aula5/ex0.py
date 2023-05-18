import math

nota1=float(input('Digite o valor da nota 1:'))
nota2=float(input('Digite o valor da nota 2:'))
nota3=float(input('Digite o valor da nota 3:'))
nota4=float(input('Digite o valor da nota 4:'))
nota5=float(input('Digite o valor da nota 5:'))

NotaA = (nota1 + nota2 + nota3 + nota4 + nota5) /5

print('A nota A é:', NotaA)

NotaB=float(input('Digite o valor da prova'))

media= (NotaA + NotaB) /2

print ('A média é:', media)

if media>=6:
    print('Aprovado!')
elif media>=4:
    print('Recuperaçâo')
else:
    print('Reprovado!')
