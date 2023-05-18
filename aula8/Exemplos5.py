def contar_vogais(texto):
    vogais = ['a', 'e', 'i', 'o', 'u']
    
    num_vogais = 0
    
    for letra in texto:
        if letra.lower() in vogais:
            num_vogais += 1
    
    return num_vogais

texto = input('Digite um texto:')
print(contar_vogais(texto))