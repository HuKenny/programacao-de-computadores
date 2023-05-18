salario=float(input('Digite o valor do seu salário:'))
gastos=float(input('Digite o valor que você gasta por mês:'))

if salario > gastos:
    print('Gastos dentro do orçamento!')
else:
    print('Orçamento estourado!')