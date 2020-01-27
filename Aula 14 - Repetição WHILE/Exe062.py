# Exe062 - Melhore o exe061 dando:
# A opção de continuar a PA e pare quando o valor for igual a 0.

print('Calculadora de PA')
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão da PA: '))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while contador <= total:
        print('{}'.format(termo), end=' > ')
        termo += razão
        contador += 1
    print('PAUSA')
    mais = int(input('\nMais quantos termo deseje acrescentar?: '))
print('Finalizado com {} termos'.format(total))
