num1=int(input('Digite o valor do primeiro número inteiro:'))
num2=int(input('Digite o valor do segundo número inteiro:'))

if num1 <=0 or num2 <=0:
    print ('Não é possível ler esses números')
elif num1 > num2:
    print('os números em ordem crescente é:', num2 , num1)
else:
    print('os números em ordem crescente é:', num1 , num2)