# Exe092 - Guarde Nome, Nascimento e carteira de trabalho num dicionario, se
# tiver CTPS: Ano de contratação, Salario e calcule Idade e ano de Aposentadoria.

from datetime import datetime
ano_atual = datetime.now().year

cadastro = {

    'Nome': str(input('Nome: ')),
    'Nascimento': int(input('ANO de Nascimento: ')),
    'CTPS': int(input('Nº da CTPS [0 se N/A]: '))

}

cadastro['Idade'] = ano_atual - cadastro['Nascimento']
cadastro['Aposentadoria'] = 75 - cadastro['Idade']

if cadastro['CTPS'] != 0:
    cadastro['Salario'] = float(input('Salário: R$'))
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['Aposentadoria'] = \
        75 - (ano_atual - cadastro['Contratação'])\
        - cadastro['Idade']

print(f'{"CADASTRO":-^30}')

for k, v in cadastro.items():
    print(f'{k} = {v}')
