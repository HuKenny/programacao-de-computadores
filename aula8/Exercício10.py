def calcular_valor_total(produtos):
    valor_total = 0
    
    for preco in produtos.values():
        valor_total += preco
    
    return valor_total

meus_produtos = {"Pera": 8, "Laranja": 15, "Morango": 10}
total = calcular_valor_total(meus_produtos)
print(total)
