num1=int(input('Digite o valor do primeiro número inteiro:'))
num2=int(input('Digite o valor do segundo número inteiro:'))

if num1 == num2:
    print('Não pode haver números iguais')
elif num1 > num2:
    print('O maior número é', num1)
else:
    print('O maior número é', num2)