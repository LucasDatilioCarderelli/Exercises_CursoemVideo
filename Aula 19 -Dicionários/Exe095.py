# Exe95 - Coloque num dicionário e mostre: nome, partidas e quantidade de gols.
# Crie uma lista de jogadores e suas estatisticas.

Ficha = {}
Time = []

print(f'{"Quantidade de Gols por JOGADOR":=^50}')

while True:
    # #### VARIAVEIS. #####
    Ficha['Nome'] = str(input('Nome do jogador: '))
    Jogos = int(input(f'Quantas partidas {Ficha["Nome"]} jogou?: '))

    # #### QUANTIDADE DE GOLS POR PARTIDA. #####
    gols_partida = []
    tot_gols = 0
    for g in range(Jogos):
        gols_partida.append(int(input(f' Quantos gols no {g + 1}ª jogo?: ')))
        tot_gols += gols_partida[g]
    Ficha['Gols'] = gols_partida
    Ficha['Total'] = tot_gols

    # #### INSERINDO FICHA NA LISTA. #####
    Time.append(Ficha.copy())
    Ficha.clear()

    # #### ALERTA PARA PARADA. #####
    while True:
        parada = str(input('CONTINUAR? [S/N]: ')).upper().strip()[0]
        if parada in 'SN':
            break
        else:
            print('ERROR!: Digite Novamente! [S/N]')
    print(f'{"=":=^50}')

    # #### SAINDO DO LOOP #####
    if parada == 'N':
        break
print(f'{" RESULTADOS ":=^50}')

# #### MOSTRAR RESULTADOS #####
print(f'{"Cod.":<15}{"Nome do Jogador":<15}{"Gols":<15}{"Total":<15}')
# print('Cod.', end='')
# for i in ficha.keys:
#     print(f'{i:<15}', end='')
# print()
for k, v in enumerate(Time):
    print(f'{k:<15}', end='')
    for c in v.values():
        print(f'{str(c):<15}', end='')
    print()
print(f'{" EXE 095 ":=^50}')

# #### MOSTRAR JOGADOR #####
while True:
    busca = int(input('Digite o Codigo do jogador para analisar, [999 = PARAR]: '))
    if busca == 999:
        break
    elif busca >= len(Time):
        print('Error!: Codigo Errado!')
    else:
        print(f' LEVANTAMENTO de {Time[busca]["Nome"]}')
        for c, g in enumerate(Time[busca]["Gols"]):
            print(f'    No jogo {c+1} fez {g} gols.')
    print(f'{"=":=^50}')
print(f'{" EXE 095 ":=^50}')
