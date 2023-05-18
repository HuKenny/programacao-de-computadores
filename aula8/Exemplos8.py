def aplica_funcao(x, f):
    return f(x)

def quadrado(x):
    return x ** 2

resultado = aplica_funcao(3, quadrado)
print(resultado)
