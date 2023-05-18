def encontrar_maior(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior

lista = [10, 5, 20, 30, 15]
print(encontrar_maior(lista))
    
    
    