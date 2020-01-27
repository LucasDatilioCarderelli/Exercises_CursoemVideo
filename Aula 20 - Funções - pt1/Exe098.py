# Exe098 - Crie uma função para uma sequencia e digite os parametros: Inicio, fim, e passo.
# execute uma contagem de: a) 0 até 10 de 1 em 1, b) 10 até 0 de 2 em 2 c) Personalizado.

from time import sleep


def seq():
    a = 10
    for c in range(0, 10):
        print(a, end=', ')
        a -= 1
        sleep(0.3)
    print('Fim...')

    b = 0
    for c in range(0, 5):
        print(b, end=', ')
        b += 2
        sleep(0.5)
    print('Fim...')


# seq()


def sequencia(i, f, p):
    if i < f:
        while i < f:
            print(i, end=', ')
            i += p
            sleep(0.3)
        print('Fim...')
    else:
        while f < i:
            print(i, end=', ')
            i -= p
            sleep(0.3)
        print('Fim...')


inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
sequencia(inicio, fim, passo)
