# Exe093 - Coloque num dicionário e mostre: nome, partidas e quantidade de gols.

Ficha = {}
gols_partida = []
tot_gols = 0

Ficha['Nome'] = str(input('Nome do jogador: '))
Ficha['Jogos'] = int(input('Quantas partidas jogadas?: '))

for g in range(Ficha['Jogos']):
    gols_partida.append(int(input(f' Quantos gols no {g+1}ª jogo?: ')))
    tot_gols += gols_partida[g]
Ficha['Gols'] = gols_partida
Ficha['Total'] = tot_gols
print(f'{" EXE 093 ":=^50}')

print(Ficha)
print(f'{" EXE 093 ":=^50}')

for k, v in Ficha.items():
    print(f'{k}: {v}')
print(f'{" EXE 093 ":=^50}')

print(f'O jogador {Ficha["Nome"]} jogou {Ficha["Jogos"]} partidas:')
count = 0
for v in Ficha['Gols']:
    count += 1
    print(f' => Na partida {count}, fez \033[32m{v}\033[m gols.')
print(f'Total de gols {Ficha["Total"]}')
print(f'{" EXE 093 ":=^50}')
