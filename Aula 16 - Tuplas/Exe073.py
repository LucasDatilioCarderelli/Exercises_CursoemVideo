# Exe073 - Preencha uma tupla com os 20 primeiros da tababela do brasileirão e tenha:
# Os 5 primeiros colocados, os ultimos 4, em ordem alfabetica e a posição do Chapecoense.

tabela = ('Santos', 'Palmeiras', 'Flamengo', 'Atlético', 'São Paulo',
          'Internacional', 'Atlético-PR', 'Corinthians', 'Goiás', 'Botafogo',
          'Grêmio', 'Bahia', 'Ceará SC', 'Fortaleza', 'Vasco da Gama',
          'Cruzeiro', 'Fluminense', 'Chapecoense', 'CSA', 'Avaí')
print(f'{"Brasileirão":=^80}')
print(f'Os 5 primeiros são:\n'
      f'{tabela[0:5]}')
print(f'{"Brasileirão":=^80}')
print(f'Os 4 ultimos são:\n'
      f'{tabela[-4:]}')                                                         # {tabela[16:20]}
print(f'{"Brasileirão":=^80}')
print(f'Os times em ordem alfabetica é:\n'
      f'{sorted(tabela)}')
print(f'{"Brasileirão":=^80}')
print(f'O Chapecoense está na posição {tabela.index("Chapecoense")+1}º Lugar.')
print(f'{"Brasileirão":=^80}')



