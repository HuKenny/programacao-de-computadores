def menornumero (num1, num2):
    if num1 < num2: 
        return num1
    else:
        return num2
    
num1 = int(input('Digite um valor para o primeiro numero:'))
num2 = int(input('Digite um valor para o segundo numero:'))

print(menornumero(num1, num2))