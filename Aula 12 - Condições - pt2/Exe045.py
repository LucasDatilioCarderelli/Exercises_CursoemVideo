# Exe045 - JO KEN PÔ!
# Modulos
from random import choice
from time import sleep
# Cores
cor = {'Limpa': '\033[m', 'vermelho': '\033[1;31m', 'verde': '\033[1;32m',
       'Amarelo': '\033[1;33m,', 'azul': '\033[1;34m', 'negativo': '\033[7;30m'}
for c in range(0, 3):
    # Player Choice
    print('{}+-'.format(cor['negativo']) * 5, 'JO KEN PÔ!', '+-' * 5, '{}'.format(cor['Limpa']))
    escolha = int(input('''
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
Escolha: '''))
    # Escolha Errada
    if escolha != 1 and escolha != 2 and escolha != 3:
        print('Error01: Escolha Outro!')
        exit()
    # Machine Choice
    lista = [1, 2, 3]
    escolhapc = choice(lista)
    # Play
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ!')
    sleep(0.5)
    # Victory Condition
    if escolha == escolhapc:                                          # Draw
        print('{}EMPATE{}!'.format(cor['Amarelo'], cor['Limpa']))
    elif escolha == 1 and escolhapc == 3 or \
            escolha == 2 and escolhapc == 1 or \
            escolha == 3 and escolhapc == 2:                          # Player Win
        print('{}VITORIA{}!'.format(cor['verde'], cor['Limpa']))
    # elif escolha == 2 and escolhapc == 1:                           # Player Win: Papel x Pedra
    #     print('{}VITORIA{}!'.format(cor['verde'], cor['Limpa']))
    # elif escolha == 3 and escolhapc == 2:                           # Player Win: Tesoura x Papel
    #     print('{}VITORIA{}!'.format(cor['verde'], cor['Limpa']))
    else:  # Player Lose
        print('{}DERROTA{}!'.format(cor['vermelho'], cor['Limpa']))
    sleep(0.5)
    # Ending
    print('Você escolheu {} e a maquina {}'.format(escolha, escolhapc)
          .replace('1', 'PEDRA').replace('2', 'PAPEL').replace('3', 'TESOURA'))
    print('{}+-'.format(cor['negativo']) * 5, 'JO KEN PÔ!', '+-' * 5, '{}'.format(cor['Limpa']))
    sleep(1.5)
