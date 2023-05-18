import datetime
ano_de_nascimeto=int(input('Digite o ano que você nasceu:'))

data_atual= datetime.date.today()

ano_atual= data_atual.year

idade = ano_atual - ano_de_nascimeto

if idade <= 18:
    print('Você pode votar!')
else:
    print('Você não pode votar!')
