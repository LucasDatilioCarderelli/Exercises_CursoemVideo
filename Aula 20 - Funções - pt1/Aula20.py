print()     # Chamando a Função
# def lin():
#     print('-' * 30)
#
#
# lin()
# print(f'{"Curso em VÍDEO":^30}')
# lin()
# print(f'{"Aprenda Python":^30}')
# lin()
print()     # Função com Paramentros
# def titulo(txt):
#     print('-' * 30)
#     print(txt)
#     print('-' * 30)
#
#
# titulo(f'{"Curso em VÍDEO":^30}')
# titulo(f'{"Aprenda Python":^30}')
print()     # Atribuindo variaveis
# def soma(a, b):
#     print(f'a = {a} e b = {b}')
#     s = a + b
#     print(f'A soma de a + b = {s}')
#
#
# soma(a=4, b=5)
# soma(b=8, a=9)
# soma(2, 0)
print()     # * = Desempacotar
# def contador(*num):
#     print(num)
#     for valor in num:
#         print(valor, end=', ')
#     print('Fim...')
#
#
# contador(2, 1)
# contador(8)
print()     # Função com Lista
# def dobra(lista):
#     pos = 0
#     while pos < len(lista):
#         lista[pos] *= 2
#         print(lista[pos], end=', ')
#         pos += 1
#     print('Fim...')
#
#
# valores = [1, 2, 5, 3, 4, 3]
# print(valores)
# dobra(valores)
# print(valores)

print('Calculadora de ADIÇÃO (digite "0" para parar)')


def soma():
    calc = []
    cont = 0
    while True:
        num = (int(input(f'Nº{cont + 1}: ')))
        if num == 0:
            break
        calc.append(num)
        cont += 1

    s = 0
    for valor in calc:
        s += valor
    print(f'A soma total é {s}')


def ligar():
    while True:
        soma()
        parada = str(input('CONTINUAR? [S/N]: ')).upper().strip()[0]
        if parada == 'N':
            break


ligar()
