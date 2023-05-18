angulo1=float(input('Digite o valor do primeiro angulo em graus:'))
angulo2=float(input('Digite o valor do segundo angulo em graus:'))
angulo3=float(input('Digite o valor do terceiro angulo em graus:'))

if angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
    print('Esse é um triangulo de ângulo obtuso!!')
elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
    print('Esse é um triangulo com ângulo reto')
else:
    print('Esse é um triangulo que possui três ângulos agudos')