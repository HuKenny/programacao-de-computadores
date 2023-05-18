def media(lista):
    soma = 0
    for numero in lista:
        soma+=numero
    return soma / len(lista)

numeros = [10,20,30,40]
resultados = media(numeros)
print(resultados)

