
palavra = input("Digite uma palavra: ")

num_vogais = 0

for letra in palavra:
    if letra.lower() in "aeiou":
        num_vogais += 1
print("O número de vogais na string é:", num_vogais)