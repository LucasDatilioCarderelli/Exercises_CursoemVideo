# Exe056 - Digite: nome, idade e sexo de 4 pessoas,
# analise: A media de idade, o nome do mais velho e quantas mulheres  <20 anos.

s = 0
c = 0
cf = 0
maiori = 0
maiorim = 0
nomev = ''
for a in range(1, 4+1):
    print('{} {}ª Pessoa {}'.format('-='*5, a, '=-'*5))
    nome = str(input('Qual o nome?: ').strip())
    idade = int(input('Qual a idade?: ').strip())
    sexo = str(input('Qual o sexo [M/F]?: ').strip().upper())
    s = s + idade
    c = c + 1
    if a == 1 and sexo == 'M':
        maiori = idade
        nomev = nome
    else:
        if idade > maiori:
            maiori = idade
            nomev = nome
    if sexo == 'F':
        if idade < 20:
            cf = cf + 1
media = s / c
print('A media das idades é {}:'.format(media))
print('Tem {} mulheres menores que 20 anos'.format(cf))
print(f'O nome do home mais velho é {nome} e tem {idade}')
