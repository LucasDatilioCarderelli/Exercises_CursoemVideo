# Exe078 - Digite 5 números e tenha o maior, menor e suas posições.
menor = maior = 0
números = []
for a in range(0,5):
    números.append(int(input(f'Digite o valor na {a+1}º posição: ')))
    if a == 0:
        maior = números[a]
        menor = números[a]
    else:
        if números[a] > maior:
            maior = números[a]
        if números[a] < menor:
            menor = números[a]
print(números)
print(f'\nO maior número é {maior} na posição, ', end='')
for c, n in enumerate(números):
    if n == maior:
        print(c, end=', ')
print(f'\nO menor número é {menor} na posição, ', end='')
for c, n in enumerate(números):
    if n == menor:
        print(c, end=', ')


# print(f'O maior número da lista é {max(números)} '
#       f'na {números.index(max(números))+1}º posição')
# print(f'O menor número da lista é {min(números)} '
#       f'na {números.index(min(números))+1}º posição')
