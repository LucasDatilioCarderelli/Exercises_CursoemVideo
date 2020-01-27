# Exe060 - Calculo de fatorial.
# n! = n * (n - 1) * (n - 2)...

# from math import factorial
# num = int(input('Digite um número: '))
# f = factorial(num)
# print(f)

num = int(input('Digite um número: '))
contador = num
fatorial = 1
while contador > 0:
    print('{}'.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end=' ')
    fatorial *= contador
    contador -= 1
print('{}'.format(fatorial))
