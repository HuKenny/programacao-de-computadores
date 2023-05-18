import math

def area_do_circulo ():
    raio=float(input("Digite o valor do raio:"))
    
    area= math.pi*(raio**2)
    
    print(f'A área do circulo é: {area:.2f}')

area_do_circulo()