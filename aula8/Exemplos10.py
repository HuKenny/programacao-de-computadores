def pessoa_mais_velha(dicionario):
    nome, idade = max(dicionario.items(), key=lambda x: x[1])
    return nome

nomes_idades = {'Alice': 30, 'Maria': 25, 'Carol': 40, 'Davi': 35}
nome_mais_velho = pessoa_mais_velha(nomes_idades)
print(nome_mais_velho) 
