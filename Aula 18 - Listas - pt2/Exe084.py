# Exe084 - Digite nomes e pesos e tenha: Quantas pessoas cadatradas;
# Uma lista das mais leves; Uma Lista das mais pesadas.

Geral = []
Cadastro = []
maior = menor = 0
print(f'{"Bem Vindo":-^30}')
while True:
    Cadastro.append(str(input('Nome: ')))
    Cadastro.append(float(input('Peso: ')))
    if len(Geral) == 0:
        maior = menor = Cadastro[1]
    else:
        if Cadastro[1] > maior:
            maior = Cadastro[1]
        elif Cadastro[1] < menor:
            menor = Cadastro[1]
    Geral.append(Cadastro[:])
    Cadastro.clear()
    parada = str(input('Continuar? [S/N]: '))
    if parada in 'Nn':
        break
    print('-'*30)
print(f'{"Encerrando":-^30}')
print(f'Total Cadastrados: {len(Geral)}')
print(f'O maior peso foi {maior} de', end=' ')
for p in Geral:
    if p[1] == maior:
        print(p[0], end=', ')
print(f'\nO menor peso foi {menor} de', end=' ')
for p in Geral:
    if p[1] == menor:
        print(p[0], end=', ')
