# Exe103 - Crie uma função que recebe parâmetro opcional, nome e qntd. gols.


def lista_jogador(nome='<jogador>', gols=0):
    print(f'O jogador {nome} fez {gols} gols')


n = str(input('Nome do Jogador: '))
g = input('Qntd. de Gols: ')

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    lista_jogador(gols=g)
else:
    lista_jogador(n, g)
