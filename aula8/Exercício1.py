def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fatorial(num - 1)

num= int(input("digite um numero:"))

print(fatorial(num))