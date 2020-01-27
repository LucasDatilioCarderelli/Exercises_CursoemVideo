# Exe089 - Crie uma lista com os nome e notas e media dos alunos,
# depois mostre suas notas

boletins = []
aluno = []
while True:
    aluno.append(str(input('Nome do aluno: ')))
    aluno.append(float(input('Nota da P1: ')))
    aluno.append(float(input('Nota da P2: ')))
    boletins.append(aluno[:])
    aluno.clear()
    parada = str(input('Continuar? [S/N]: '))
    if parada in 'Nn':
        break
print('-='*15)
print(f'{"Nº.": <5}{"Nome do Aluno(a)":<20}{"MÉDIA":<3}')
print('-'*30)
for i, p in enumerate(boletins):
    media = (boletins[i][1] + boletins[i][2]) / 2
    print(f'{i:<5}{boletins[i][0]:<20}{media:<3.1f}')
print('-='*30)
while True:
    opção = int(input('Deseja saber as notas de qual aluno(a)? [999 Encerra]: '))
    if opção == 999:
        break
    print(f'A as notas do Aluno, {boletins[opção][0]}, são, '
          f'{boletins[opção][1]} e {boletins[opção][2]}')
    print('-'*60)
print('-='*30)
