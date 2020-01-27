# Exe087 - MEGA SENA: Sorteie 6 números para cada jogo numa lista composta.

from random import randint
from time import sleep

ListaJogos = []
sorteio = []
jogos = int(input('Quantos veses vai jogar?: '))
cont = tot = 0
while tot != jogos:
    while True:
        aleatorio = randint(1, 60)
        if aleatorio not in sorteio:
            sorteio.append(aleatorio)
            cont += 1
            if cont >= 6:
                break
    sorteio.sort()
    ListaJogos.append(sorteio[:])
    sorteio.clear()
    tot += 1
    cont = 0
print(f'{"Gerando...":-^30}')
for v in range(0, len(ListaJogos)):
    sleep(1)
    print(ListaJogos[v], end='')
    print()
