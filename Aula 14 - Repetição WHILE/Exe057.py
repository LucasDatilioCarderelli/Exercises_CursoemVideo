# Exe057 - Digite o sexo de uma pessoa e repita quando for diferente de F ou M.

sexo = str(input('Digite o sexo da pessoa [F/M]: ').upper().strip()[0])
while sexo not in 'MF':
    sexo = str(input('Você digitou sexo errado, Repita!: ').upper().strip()[0])
print('Validado com SUCESSO')
