# Exe087 - Crie uma matriz e tenha: A soma da 1º linha; A soma da 3º coluna,
# E o maior valor da terceira linha.

print(f'{"Analise de Matriz":-^36}')
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maior = contpar = somal = somac = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor da posição [{l}][{c}]: '))
        if matriz[l][c] % 2 == 0:
            contpar += matriz[l][c]
        if l == 1 and c == 0:
            maior = matriz[l][c]
        elif l == 1:
            if matriz[l][c] > maior:
                maior = matriz[l][c]
print('-' * 36)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^4}]', end='')
    print()
print(f'{"Analise de Matriz":-^36}')
print(f'A soma dos pares é   : {contpar}')
# for c in range(0, 3):
#     somal += matriz[0][c]
print(f'A soma da 1º Linha é : {(matriz[0][0]) + (matriz[0][1]) + (matriz[0][2])}')
# for l in range(0, 3):
#     somac += matriz[l][2]
print(f'A Soma da 3º Coluna é: {(matriz[0][2]) + (matriz[1][2]) + (matriz[2][2])}')
print(f'O maior da 2º linha é: {maior}')
