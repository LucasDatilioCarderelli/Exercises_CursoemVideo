# Exe006 - Digite um número e tenha seu dobro, triplo e raiz quadrada.

num = float(input('Digite um número: '))
x2 = num * 2
x3 = num * 3
square = num ** (1/2)
print('\033[7mO dobro é : {}\033[m\n\033[7mO triplo é: {}\033[m\n\033[7mA raiz é : {:.2f}\033[m'.format(x2, x3, square))
