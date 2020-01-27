# Exe001 - Mostre 'Olá ,Mundo!'

cores = {'Limpa': '\033[m',
        'Azul':'\033[34m',
        'Amarelo':'\033[33m',
        'Vermelho': '\033[31m',
        'Negativo':'\033[07;30m'}

# msg = Olá, Mundo!
# print(msg)

print('\033[7;31;40mOlá, Mundo!\033[m')
print('{}Seja{} {}Muito{} {}Bem{} {}Vindo{}!'.format(cores['Azul'], cores['Limpa'],
                                                     cores['Amarelo'], cores['Limpa'],
                                                     cores['Vermelho'], cores['Limpa'],
                                                     cores['Negativo'], cores['Limpa']))

