altura=float(input('Digite a sua altura em cm:'))
sexo=int(input('Digite 1 para mulher e 2 para homem:'))

if sexo == 1:
    pesoideal=(62.1 * altura) - 44.7
    
    print(' O seu peso ideal é igual a:', pesoideal)
else:
    pesoideal= (72.7 * altura) - 58 
    
    print (' O seu peso ideal é igual a:', pesoideal)

    