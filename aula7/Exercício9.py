numeros = input("Digite uma lista de números separados por vírgula: ")

numeros = [int(num) for num in numeros.split(",")]

maior_numero = numeros[0]
menor_numero = numeros[0]

indice = 1

while indice < len(numeros):

    if numeros[indice] > maior_numero:
        maior_numero = numeros[indice]
    if numeros[indice] < menor_numero:
        menor_numero = numeros[indice]
    indice += 1

print("O maior número da lista é:", maior_numero)
print("O menor número da lista é:", menor_numero)