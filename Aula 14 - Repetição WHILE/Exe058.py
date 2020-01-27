# Exe058 - Jogo da adivinhação, buff Exe028.

from random import randint
from time import sleep

contagem = 0
palpite = 0
gerado = randint(0, 10)
# acertou = False
# while not acertou:
while palpite != gerado:
    # if palpite == gerado
    # acertou == True
    print('{} \033[33m ADVINHE! \033[m {}'.format('+-'*5, '-+'*5))
    palpite = int(input('Adivinhe um número de 1 a 10!: '))
    print('Vamos ver...')
    sleep(1)
    contagem = contagem + 1
    if palpite > gerado:
        print('Passou! Chute \033[31m Mais BAIXO\033[m ...')
    elif gerado > palpite:
        print('Quase lá! Chute \033[32m Mais ALTO\033[m ...')
print('\033[33mVocê acertou!\033[m Precisou de {} tentativas!'.format(contagem))
