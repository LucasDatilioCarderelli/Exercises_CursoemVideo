# Exe036 - Digite: valor da casa, salário e quantos anos de pagamento,
# calcule o valor da prestação, não podendo passar 30% do salário.

# Constantes
casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Quanto é o seu salário? R$'))
tempo = int(input('Em quantos anos será parcelado? '))
# Variaveis
prestacao = casa / (tempo * 12)
limite = salario * (30/100)
# Print Prestação
print('Uma casa que custa \033[1;32mR${:.2F}\033[m paga em \033[1;33m{}\033[manos,'
      ' o valor da prestação será de: \033[1;32mR${:.2f}\033[m'
      .format(casa, tempo, prestacao))
# Condição Salário
if limite <= prestacao:
    print('O seu salario de \033[1;32mR${:.2f}\033[m '
          '\033[1;31mNÃO\033[m tem condição de pagar \033[1;32m{:.2f}\033[m por mês '
          'pois o limite é de \033[1;32mR${:.2f}\033[m por mês'
          .format(salario, prestacao, limite))
# elif limite > prestacao
else:
    print('O seu salario de \033[1;32mR${:.2f}\033[m '
          'tem \033[1;34mSIM\033[m condição de pagar \033[1;32m{:.2f}\033[m por mês '
          'pois o limite é de \033[1;32mR${:.2f}\033[m por mês'
          .format(salario, prestacao, limite))
