# Digite o 1º número e a razão para mostrar os 10 primeiros números da PA.

n1 = int(input('Qual é o primeiro número da PA?: '))
r = int(input('Qual é a razão da PA?: '))
# decimo = n1 + (10 - 1) * r
# for c in range(n, decimo, razão)
for c in range(1, 10+1):
    a = n1 + (c - 1) * r
    print(a, end=' > ')
print('...')
