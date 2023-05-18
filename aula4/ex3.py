import math

alfaGraus = float(input('Por favor, digite o ângulo em graus:'))
alfaRad = math.radians(alfaGraus)
print(f'Obs: O equivalente em radianos deste ângulo é {alfaRad: .2f}')
print(f'O seno de  {alfaGraus: .0f} vale {math.sin(alfaRad):.4f}')
print(f'O coss de  {alfaGraus: .0f} vale {math.cos(alfaRad):.4f}')
print(f'A tangente de  {alfaGraus: .0f} vale {math.tan(alfaRad):.4f}')