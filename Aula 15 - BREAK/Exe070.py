# Exe070 - Digite o nome e valor de varios produtos e tenha:
# O total da compra, quantos produtos acima de R$1.000,00 e qual o menor produto.
cont = contn = soma = menor = 0
menorn = ' '
print(f'{"LOJINHA":-^40}')
while True:
    nome = str(input('Nome: '))
    preço = float(input('Preço: R$').strip())
    soma += preço
    contn += 1
    if contn == 1 or preço < menor:
        menor = preço
        menorn = nome
    if preço >= 1000:
        cont += 1
    parada = ' '
    while parada not in 'SN':
        parada = str(input('Mais 1 produto [S/N]?: ').strip().upper()[0])
    if parada == 'N':
        break
print(f'Total: R${soma:.2f}')
print(f'Acima de R$1.000,00: {cont}')
print(f'O menor produto custou R${menor} ({menorn}).')
print(f'{"VOLTE SEMPRE":-^40}')
