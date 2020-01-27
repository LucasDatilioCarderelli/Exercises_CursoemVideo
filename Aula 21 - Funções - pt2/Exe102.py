# Exe102 - Crie uma função fatorial com parâmetro (opcional)     'SHOW' mostrando o calculo.


def factorial(num=0, show=False):
    """
    -> Calculo de fatorial com parâmetro:
    :param num: Número a ser fatorado;
    :param show: Mostrar (True) ou Não (False) o cálculo;
    :return: Resultado.
    """
    n = num
    if show:
        print(f'{num}', end='')
    while n != 1:
        n -= 1
        num *= n
        if show:
            print(f' * {n}', end='')
    if show:
        print(f' = {num}')
    return print(f'Resulto é = {num}')


factorial(10, True)
help(factorial)

# for c in range(num, 0, -1):
#     if show:
#         print(c, end='')
#         if c < 1:
#             print(' x ', end='')
#         else:
#             print(' = ', end='')
#     num *= c
# return num