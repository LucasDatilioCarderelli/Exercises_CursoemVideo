# Exe003 - Digite dois números e some eles.

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
soma = num1 + num2
print('A soma entre {} e {} é igual a = {}{}{}'.format(num1, num2,
                                                       '\033[1;32m', soma, '\033[m'))

