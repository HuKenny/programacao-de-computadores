def soma(*args):
    resultado = 0
    for arg in args:
        resultado += arg
    return resultado

resultado1 = soma(1, 2, 3)
resultado2 = soma(10, 20, 30, 40)
resultado3 = soma(1.5, 2.5, 3.5)

print(resultado1) 
print(resultado2) 
print(resultado3)
