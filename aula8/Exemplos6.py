def quociente_resto(dividendo,divisor):
    quociente = dividendo // divisor
    resto = dividendo % divisor
    return quociente, resto

dividendo = float(input("Digite o valor do dividendo:"))
divisor = float(input("Digite o valor do divisor:"))

print('O quociente e o resto respectivamente:',quociente_resto(dividendo, divisor))