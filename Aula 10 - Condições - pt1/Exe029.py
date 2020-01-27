# Exe029 - Digite a velocidade de um carro e calcule sua multa se ultrapassar o maximo permitido sendo:
# (R$7,00 por Km/h)

limite = float(input('Qual é o limite da estrada em Km/h: '))
velocidade = float(input('Qual é a velocidade em Km/h? '))
multa = (velocidade - limite) * 7

if velocidade > limite:
    print('Você está {}Km/h acima do permitido\nDeverá pagar uma multa de R${}'
          .format(velocidade - limite, multa))
else:
    print('Você está {}Km/h abaixo do limite. Muito bom!'.format(limite - velocidade))
exit()
