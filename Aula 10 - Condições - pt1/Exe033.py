# Exe033 - Digite 3 números e descruba qual é o menor e qual o maior.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo numero : '))
n3 = int(input('Digite o terceiro número: '))

menor = n1
if n2 > n1 and n2 > n3:
    menor = n2
if n3 > n1 and n3 > n2:
    menor = n3

maior = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print('1º: {}'.format(menor))
print('2º: {}'.format(maior))
