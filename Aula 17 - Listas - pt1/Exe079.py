# Exe079 - Digite varios valores,
# coloque os diferentes em ordem numa lista.

números = list()
while True:
    n = int(input('Digite um número: '))
    if n not in números:
        números.append(n)
    r = str(input('Continuar? [S/N]: '))
    if r in 'Nn':
        break
    print('-='*10)
números.sort()
print(f'Foram adicionados {números}')
