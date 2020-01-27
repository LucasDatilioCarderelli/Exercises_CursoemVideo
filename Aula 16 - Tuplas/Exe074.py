# Exe074 - Gere 5 números numa tupla e tenha o maior e menor.

from random import randint

números = (randint(0, 9), randint(0, 9), randint(0, 9),
           randint(0, 9), randint(0, 9))
print('Os números sorteados foram: ')
for n in números:
    print(n, end=' ')
print(f'\nO maior número foi {max(números)}')
print(f'O menor número foi {min(números)}')
