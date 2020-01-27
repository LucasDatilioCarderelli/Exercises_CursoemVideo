# Exe061 - Refaça o exe 51 para calcular PA com while.

print('Calculadora de PA')
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão da PA: '))
termo = primeiro
contador = 1
print('{}'.format(primeiro), end=' > ')
while contador <= 10:
    termo += razão
    contador += 1
    print('{}'.format(termo), end=' > ')
print('...')
