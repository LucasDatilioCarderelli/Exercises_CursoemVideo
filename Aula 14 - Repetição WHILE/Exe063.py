# Exe063 - Faça a sequencia de fibonacci de um número inteiro até n termos.

print('SEQUENCIA DE FOBONACCI')
termos = int(input('Quantos termos deseja?: '))
contador = 3
t1 = 0
t2 = 1
print('{} > {}'.format(t1, t2), end=' > ')
while contador != termos:
    t3 = t1 + t2
    print(t3, end=' > ')
    t1 = t2
    t2 = t3
    contador += 1
print('...')
