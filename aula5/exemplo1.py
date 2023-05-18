num1=int(input('Digite o primeiro número:'))
num2=int(input('Digite o segundo número:'))

if num1 > num2:
    print('O primeiro, %d, é maior' %num1)
else:
    if num1 == num2:
        print('os números são iguais')
    else:
        print('O segundo, %d, é maior' %num2)