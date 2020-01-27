# Exe071 - Caixa Eletrônico, contendo cedulas de : R$50, R$20, R$10 e R$1.

contador50 = contador20 = contador10 = contador01 = 0
print(f'\033[7;30m{"CAIXA CeV":=^30}\033[m')
saque = int(input('Quanto deseja sacar? R$').strip())
while True:
    while True:
        if saque >= 50:
            saque -= 50
            contador50 += 1
        else:
            break
    while True:
        if saque >= 20:
            saque -= 20
            contador20 += 1
        else:
            break
    while True:
        if saque >= 10:
            saque -= 10
            contador10 += 1
        else:
            break
    while True:
        if saque >= 1:
            saque -= 1
            contador01 += 1
        else:
            break
    if saque == 0:
        break
print(f'O valor será sacado em:')
print(f'{contador50} Cedulas de R$50\n'
      f'{contador20} Cedulas de R$20\n'
      f'{contador10} Cedulas de R$10\n'
      f'{contador01} Cedulas de R$01')
print(f'\033[7;30m{"Volte Sempre!":=^30}\033[m')
