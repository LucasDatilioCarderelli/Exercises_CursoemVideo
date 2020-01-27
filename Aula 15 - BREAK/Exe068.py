# Exe068 - Par ou Ímpar!

from time import sleep                                                              # IMPORTAÇÕES
from random import randint
print('\033[7;30m{} !PAR OU ÍMPAR! {}\033[m'.format('+-'*6, '-+'*6))
playerN = computadorn = 0                                                           # VARIAVEIS
playerO = ''
soma = 0
cont = 0
continuar = ''
while continuar != 'N':                                                             # REPETIR ALL
    while True:                                                                     # VALOR NÚMERO
        playerN = int(input('Escolha um Número de [0 a 9]: ').strip())
        while True:
            if playerN > 9 or playerN < 0:
                print('\033[1;31mERROR\033[m: Insira o valor novamente...')
                playerN = int(input('Escolha um Número de [0 a 9]: ').strip())
            else:
                break
        playerO = str(input('Escolha Par ou Ínpar [ P/I ]: ').strip().upper()[0])   # VALOR OPÇÃO
        while True:
            if playerO != 'P' and playerO != 'I':
                print('\033[1;31mERROR\033[m: Insira o valor novamente...')
                playerO = str(input('Escolha Par ou Ínpar [ P/I ]: ').strip().upper()[0])
            else:
                break
        print('-=' * 20)
        computadorn = randint(0, 9)                                                 # PROCESSAR INFO
        soma = playerN + computadorn
        print('3')
        sleep(0.5)
        print('2')
        sleep(0.5)
        print('1')
        print(f'Você escolheu {playerO} e {playerN} e o computador {computadorn}\n'
              f'A soma deu {soma} e...' # ('Deu PAR' if soma % 2 == 0 else 'Deu ÍMPAR')
              .replace('P', 'PAR').replace('I', 'ÍNPAR'))
        if soma % 2 == 0:                                                           # CONDIÇÃO WIM PAR
            print('Deu PAR')
            if playerO == 'P':
                print('\033[1;33mPlayer WIN\033[m')
            else:
                print('\033[1;31mPlayer LOOSE\033[m')
                break
        if soma % 2 != 0:                                                           # CONDIÇÃO WIM ÍMPAR
            print('Deu ÍMPAR')
            if playerO == 'I':
                print('\033[1;33mPlayer WIN\033[m')
            else:
                print('\033[1;31mPlayer LOOSE\033[m')
                break
        cont += 1
        print('\033[7;30m{} !PAR OU ÍMPAR! {}\033[m'.format('+-' * 6, '-+' * 6))
    print(f'Você ganhou {cont} vezes, PARABÉNS!')                                   # CONTADOR
    print('-='*20)
    continuar = str(input('Deseja Continuar [S/N]?: ').strip().upper()[0])
    while True:                                                                     # CONTINUE
        if continuar != 'S' and continuar != 'N':
            print('\033[1;31mERROR\033[m: Insira o valor novamente...')
            continuar = str(input('Deseja Continuar [S/N]?: ').strip().upper()[0])
        else:
            break
print('\033[7;30m{} !PAR OU ÍMPAR! {}\033[m'.format('+-'*6, '-+'*6))                # FINALIZAÇÃO
