# Exe072 - Digite um número de 0 a 20 e tenha o número por extenso.

números = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete',
           'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
           'Quinze', 'Dezeseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    digitado = int(input('Digite um número de 0 a 20: ').strip())
    while True:
        if digitado > 20 or digitado < 0:
            print('ERROR: Opção Invalida!')
            digitado = int(input('Digite um número de 0 a 20: ').strip())
        else:
            break
    print(f'Foi digitado o número {números[digitado]}')
    parada = str(input('Deseja Repetir? [S/N]: ').strip().upper()[0])
    while True:
        if parada not in 'SN':
            print('ERROR: Opção Invalida!')
            parada = str(input('Deseja Repetir? [S/N]: ').strip().upper()[0])
        else:
            break
    if parada == 'N':
        break
print('ENCERRANDO...')