# Exe082 - Digite varios valores criando uma lista, mostre:
# Os números pares; Os números impares.

n = list()
np = list()
ni = list()
while True:
    v = (int(input('Digite um número: ')))
    n.append(v)
    if v % 2 == 0:      # for i, v enumerate(n)
        np.append(v)
    else:
        ni.append(v)
    parada = str(input('Continuar? [S/N]: '))
    if parada in 'Nn':
        break
print(n)
print(np)
print(ni)
