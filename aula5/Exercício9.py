macas_compradas=int(input('Quantas maçãs gostaria de comprar?:'))

macas_menos_duzia= 0.30
macas_mais_duzia= 0.25

if macas_compradas < 12:
    print('O total é', macas_compradas * macas_menos_duzia)
else:
    print('O total é', macas_compradas * macas_mais_duzia)