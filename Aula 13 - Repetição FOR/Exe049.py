# Exe049 - Faça uma tabuada.

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 10+1):
    print('{} x {} = {}'.format(num, c, num*c))
