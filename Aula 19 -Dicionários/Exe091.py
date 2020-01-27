# Exe091 - Gere aleatóriamente resultado de dados para 4 jogadores e
# ponha-os em ordem.

from random import randint
from time import sleep
from operator import itemgetter
jogos = {'jogador1': randint(0, 6),
         'jogador2': randint(0, 6),
         'jogador3': randint(0, 6),
         'jogador4': randint(0, 6)}
ranking = []

for k, v in jogos.items():
    sleep(0.7)
    print(f'O {k} tirou: {v}')

ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print(f'{"Ranking":#^25}')
for i, v in enumerate(ranking):
    sleep(0.7)
    print(f'{i}º Lugar: {v[0]} com {v[1]}')
