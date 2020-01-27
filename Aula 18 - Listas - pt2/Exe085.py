# Exe085 - Digite sete números e ponha-os numa lista, separando por:
# pares e ímpares em ordem crescente.

números = [[], []]

for c in range(0, 7):
    n = int(input(f'Digite o {c+1}º número: '))
    if n % 2 == 0:
        números[1].append(n)
    else:
        números[0].append(n)
números[0].sort()
números[1].sort()
print(números[0])
print(números[1])
