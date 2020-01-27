# Exe022 - Digite um nome completo e mostre: tudo em maiusculo, minusculo,
# quantas letras sem espaço, quantas letras o primeiro nome.

nome = str(input('Digite seu nome: ')).strip()
print('Maiusculo: ', nome.upper())
print('Minusculo: ', nome.lower())
print('Seu nome tem: ', len(nome) - nome.count(' '))
# L = nome.split()
# print(len(''.join(L)))

# print(nome.find(' '))
nome1 = nome.split()
print('Seu 1º nome é', nome1[0], 'e tem', len((nome1[0])), 'letras.')
