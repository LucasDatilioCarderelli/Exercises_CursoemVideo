num = [2, 3, 4, 5]
print(num)
num[2] = 3
print(num)
num.append(1)
print(num)
num.sort(reverse=True)
print(num)
num.insert(2, 0)
print(num)
num.pop()
print(num)
if 3 in num:
    num.remove(3)
else:
    print('Não tem o num 3')
print(num)
print(f'A lista tem {len(num)} números')

# valores = list()
# valores.append(1)
# valores.append(2)
# valores.append(3)
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor: ')))
#
# for c, v in enumerate(valores):
#     print(f'Na posção {c} temos {v}...')
# print('End')

a = [1, 2, 3, 4]
b = a[:]
b[2] = 8
print(f'{a}\n{b}')
