lado1=float(input('Digite o valor do primeiro lado em cm:'))
lado2=float(input('Digite o valor do segundo lado em cm:'))
lado3=float(input('Digite o valor do terceiro lado em cm:'))

if lado1 == lado2 == lado3:
    print('Esse é um triangulo Equilátero!!')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('Esse é um triangulo Isóscele')
else:
    print('Esse é um triangulo Escaleno')