# Exe028 - Tenha um número aleatorio e adivinhe-o.

import random
from time import sleep
# from random import randint
# escolhido = randint(0, 5)
lista = [1, 2]
escolhido = random.choice(lista)
na = int(input('Adivinhe um número entre 1 e 2: '))
print('Pensando...')
sleep(1.5)
if na == escolhido:
    print('Você acertou!')
else:
    print('Você errou!')
    print('O PC escolheu o número', escolhido)
