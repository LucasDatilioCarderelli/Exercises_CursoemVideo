# Exe094 - Leia: Nome, Sexo e Idade guardando num dicionário e coloque-o numa lista.
# Mostre: Quantidade de pessoas, Média de idade, Uma lista de Mulheres, Uma lista com
# Idade acima da média.

sistema = []
pessoa = {}
soma_idade = 0

while True:
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Idade'] = int(input('Idade: '))
    soma_idade += pessoa['Idade']
    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoa['Sexo'] != 'M' and pessoa['Sexo'] != 'F':
            print('ERROR!: Digite Corretamente [M/F]!')
        else:
            break
    sistema.append(pessoa.copy())
    pessoa.clear()
    while True:
        parada = str(input('Continuar? [S/N]: ')).upper().strip()[0]
        if parada != 'S' and parada != 'N':
            print('ERROR!: Digite Corretamente [S/N]!')
        else:
            break
    print(f'{" EXE 094 ":=^35}')
    if parada == 'N':
        print(f'{" Gerando Estatistica ":=^35}')
        break

print(f'Total Cadastrados: {len(sistema)}')
print()
print(f'{" EXE 094 ":=^35}')


media_idade = soma_idade/len(sistema)
print(f'Média das idades: {media_idade:5.2f}')
print()
print(f'{" EXE 094 ":=^35}')


print('Nome de TODAS as Mulheres: ')
for p in sistema:
    if p['Sexo'] in 'F':
        print(f' {p["Nome"]}', end=',')
print()
print()
print(f'{" EXE 094 ":=^35}')


print('Nome de TODOS(as) pessoas com idade acima da Média: ')
for p in sistema:
    if p['Idade'] >= media_idade:
        print(f'{p["Nome"]}, com {p["Idade"]}', end=',')
print()
print(f'{" EXE 094 ":=^35}')
