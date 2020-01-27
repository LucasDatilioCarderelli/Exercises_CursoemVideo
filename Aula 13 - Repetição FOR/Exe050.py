# Exe050 - DIGITE 6 números inteiros e some os pares.

s = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite {}º número inteiro: '.format(c)))
    if num % 2 == 0:
        cont += 1
        s = s + num
print('a some dos {} é {}'.format(cont, s))
