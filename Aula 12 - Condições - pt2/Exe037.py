# Exe037 - Digite um número inteiro e convertando para,
# (1) para binario, (2) para octal (3) para hexadecimal.

num = int(input('Digite um número inteiro: '))
print('''Aperte para converter:
[ 1 ] para binario
[ 2 ] para octal
[ 3 ] para hexadecimal''')
escolha = int(input('Sua opção: '))
if escolha != 1 and escolha != 2 and escolha != 3:
    print('Erro: opção não existente!')
elif escolha == 1:
    print('O número {} em binario é: {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('O número {} em octal é: '.format(num, oct(num)[2:]))
elif escolha == 3:
    print('O número {} em hexadecimal é: '.format(num, hex(num)[2:]))


