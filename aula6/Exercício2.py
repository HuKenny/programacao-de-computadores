import math

numerosdelados=int(input('Digite o valor dos lados do polígono:'))
medidadoslados=float(input('Digite o valor da medida dos lados em cm:'))

if numerosdelados == 3:
    area = (medidadoslados * medidadoslados)/2
  
    print('Triângulo com área igual a:', area)
elif numerosdelados == 4:
    area = (medidadoslados**2)
    
    print('Qadrado com área igual a:', area)
elif numerosdelados ==5:
    area = ((5*(numerosdelados * medidadoslados * math.sqrt(3))) /4)
    
    print('Pentágono com área igual a:',area)
else:
    print('POLÍGONO NÃO IDENTIFICADO')

    
    