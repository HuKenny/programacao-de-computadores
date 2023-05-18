numeros1 = input("Digite a primeira lista de números separados por vírgula: ")
numeros2 = input("Digite a segunda lista de números separados por vírgula: ")

numeros1 = [int(num) for num in numeros1.split(",")]
numeros2 = [int(num) for num in numeros2.split(",")]

lista_resultante = []

for num in numeros1:
    lista_resultante.append(num)

for num in numeros2:
    lista_resultante.append(num)


print("A lista resultante da concatenação das duas listas é:", lista_resultante)
