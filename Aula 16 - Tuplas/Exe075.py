# Exe075 - Digite 4 números e tenha:
# Quantidade de 9, 1º posição do 3 e quantos números pares.

num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
num3 = int(input('Digite o 3º número: '))
num4 = int(input('Digite o 4º número: '))
tupla = (num1, num2, num3, num4)
print(f'Os números digitados foram: {tupla}')
print(f'O número 9 apareceu {tupla.count(9)} veses;')
if 3 in tupla:
    print(f'O  1º número 3 apareceu na posição {tupla.index(3)+1}º;')
else:
    print('O número 3 não apareceu')
print(f'Os número(s) par(es) são:', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=', ')

# nums(int(input('Digite o 1º número: ')),
#      int(input('Digite o 2º número: ')),
#      int(input('Digite o 3º número: ')),
#      int(input('Digite o 4º número: ')))
