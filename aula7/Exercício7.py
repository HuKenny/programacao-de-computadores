palavra = input("Digite uma palavra: ")

palavra_reversa = ""

indice = len(palavra) - 1

while indice >= 0:

    palavra_reversa += palavra[indice]

    indice -= 1
print("A palavra ao contrário é:", palavra_reversa)