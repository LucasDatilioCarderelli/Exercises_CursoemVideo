# Exe081 - Digite varios números colocando numa lista, mostre:
# Quantos números foram digitados; Em ordem decrescente e se tem 5.

números = list()
c = 0
while True:
    n = int(input('Digite um número: '))    # números.append(input...)
    números.append(n)
    parada = input('Continuar? [S/N]: ')
    c += 1
    print('-='*10)
    if parada in 'Nn':
        break
print(c)                                    # print(len(números))
números.sort(reverse=True)
print(números)
if números.count(5) >= 1:                   # if 5 in números:
    print('Tem 5')
else:
    print('N Tem 5')

