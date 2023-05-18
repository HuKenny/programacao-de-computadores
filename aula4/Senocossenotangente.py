# Exemplo 1: Elaborar um progama em Python para calcular os de seno, cosseno e tangente de um ângulo alfa fornecido pelo usuário, em radianos 
# obs: como as funçôes sin, cos e tan do Python recebem um ângulo em radianos, podemos realizar o cálculo diretamente.

import math

alfa = float(input(' Por favor, digite o ângulo em radianos:'))

print(' O seno de', round(alfa,2), 'vale', round(math.sin(alfa),4))
print(' o cosseno de', round(alfa,2), round(math.cos(alfa),4))
print('A tangente de', round(alfa,2), round(math.tan(alfa),4))