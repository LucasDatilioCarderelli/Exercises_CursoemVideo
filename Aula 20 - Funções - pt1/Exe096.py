# Exe096 - Cálculo de area com função.

print(f'{"Cálculo de ÁREA":-^31}')


def área(comprimento, largura):
    a = comprimento * largura
    print(f'A área de {c}m * {l}m é =\n{a}m^2')


c = float(input('Comprimento: '))
l = float(input('Largura    : '))
área(c, l)


# def área():
#     comprimento = float(input('Comprimento: '))
#     largura = float(input('Largura    : '))
#     resultado = comprimento * largura
#     print(f'A área de {comprimento}m * '
#           f'{largura}m é =\n{resultado}m^2')
#
#
# área()
