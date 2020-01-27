# Exe016 - Digite um número e mostre a sua parte interira.

# import math
from math import floor, trunc
num = float(input('Digite um número: '))
print('O número {} tem {} inteiros'.format(num, floor(num)))
print()
num2 = float(input('Digite outro número: '))
print('O número {} tem {} inteiros'.format(num2, trunc(num2)))
print()
num3 = float(input('Digite mais um número: '))
print('O número {} tem {} inteiros'.format(num3, (int(num3))))
