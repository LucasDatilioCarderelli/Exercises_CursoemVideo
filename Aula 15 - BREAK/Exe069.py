# Exe069 - Digite a idade e sexo de varias pessoas perguntando se quer continuar,
# Analise: quantas pessoas é maior de 18 anos, quantos homens, quantas mulheres menores de 20 anos.
maiorI = homens = mulheresM = cadastro = 0
while True:
    print(f'{"-" * 27}\n   |CADASTRE UMA PESSOA| \n{"-" * 27}')
    idade = int(input('Idade: '))
    while True:
        if idade < 0 or idade > 150:
            print('ERROR: Opção invalida!')
            idade = int(input('Idade: '))
        else:
            break
    if idade >= 18:
        maiorI += 1
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    while sexo != 'M' or sexo != 'F':
        if sexo != 'M' and sexo != 'F':
          print('Erro: Opção Invalida!')
          sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        else:
            break
    if sexo == 'M' and idade < 20:
        mulheresM += 1
    parada = input(f'{"-" * 27}\nDeseja Continuar? [S/N]: ').strip().upper()[0]
    while True:
        if parada != 'S' and parada != 'N':
            print('Error: Opção invalida!')
            parada = input(f'{"-" * 23}\nDeseja Continuar? [S/N]: ').strip().upper()[0]
        else:
            break
    if parada == 'N':
        print(f'{"-" * 27}\nENCERRANDO...')
        break
print(f'São no total {cadastro} cadastros;'
      f'São no total {homens} homens;\n'
      f'São no total {maiorI} maiores de idade;\n'
      f'E são {mulheresM} mulheres menores de 20 anos.')
