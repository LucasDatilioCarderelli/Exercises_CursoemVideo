# Exe076 - Crie uma tupla unica com nome e respectivo preços dos produtos e
# crie uma tabela.

print('-' * 50)
print(f'{"MATERIAL ESCOLAR":^50}')
print('-' * 50)
materiais = ('Apontador', 1.50,
             'Borracha', 1.00,
             'Caderno', 30.00,
             'Caneta', 2.00,
             'Compasso', 5.50,
             'Estojo', 10.00,
             'Lápis', 1.50,
             'Livros', 70.00,
             'Mochila', 120.00)
for pos in range(0, len(materiais)):
    if pos % 2 == 0:
        print(f'{materiais[pos]:.<40}', end='')
    else:
        print(f' R${materiais[pos]:>7.2f}')
print('-' * 50)
