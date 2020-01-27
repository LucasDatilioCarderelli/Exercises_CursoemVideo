# Exe052 - Digite um número e descubra se ele é primo.

div = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end=' ')
        div = div + 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print('\033[m')
if div == 2:
    print('Esse número, SIM é primo')
else:
    print('Esse número, NÃO é primo')
