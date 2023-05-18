def texto_mais_longo(*textos):
    mais_longo = ''
    for texto in textos:
        if len(texto) > len(mais_longo):
            mais_longo = texto
    return mais_longo

texto1 = input("Digite o texto1:")
texto2 = input("Digite o texto2:")
texto3 = input("Digite o texto3:")

print(texto_mais_longo(texto1,texto2,texto3))