# Exe090 - Digite nome, média e situação do aluno num dicionário.

aluno = {}
# aluno = dict()

aluno['nome'] = str(input('Nome do aluno(a): '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 < aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f' - {k} é igual a {v}')

# print(f' - Aluno: {aluno["nome"]}\n'
#           f' - Média: {aluno["média"]}\n'
#           f' - Situação: {aluno["situação"]}')
