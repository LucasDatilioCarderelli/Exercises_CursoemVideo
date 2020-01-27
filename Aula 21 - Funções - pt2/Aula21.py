print()     # Ajuda Interativa
# help(input)
# print(input.__doc__)

print()     # Ajuda com docstrings
# def contador(i, f, p):
#     """
#     -> Faz uma contagem e mostra na tela
#     :param i: Início da contagem
#     :param f: Fim da contagem
#     :param p: Passo da contagem
#     :return: Sem retorno
#     """
#     c = i
#     while c < f:
#         print(c, end=', ')
#         c += p
#     print()
#
#
# contador(1, 10, 2)
# help(contador)

print()     # Parametros Opcionais
# def somar(a=0, b=0, c=0):
#     """
#     -> Função de soma números com parametros Opcionais
#     """
#     s = a+b+c
#     print(f'A soma é {s}')
#
#
# somar(1, 2, 3)
# somar(4, 5)
# somar(6)
# somar()
# print(somar.__doc__)

print()     # Escopo de variaveis
# def teste(b):
#     global a
#     a = 8
#     b += 4
#     c = 2
#     print(f"'A' dentro da f(teste) vale = {a}")
#     print(f"'B' dentro de f(teste) vale = {b}")
#     print(f"'C' dentro de f(teste) vale = {c}")
#
#
# # Programa Principal
# a = 5
# teste(a)
# print(f"'A' fora de f(teste) vale = {a}")

print()     # Retorno de valores
# def somar(a=0, b=0, c=0):
#     """
#     -> Função de soma números com parametros Opcionais
#     """
#     s = a+b+c
#     return s
#
#
# r1 = somar(1, 2, 3)
# r2 = somar(3, 3)
# r3 = somar(6)
#
# print(f'Os resultados foram {r1}, {r2} e {r3}')


def fatorrial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {fatorrial(n)}')

# help(range)


def par(p=0):
    if p % 2 == 0:
        return True
    else:
        return False


nume = int(input(f'Digite um Número: '))
if par(nume):
    print('É par')
else:
    print('É impar')
