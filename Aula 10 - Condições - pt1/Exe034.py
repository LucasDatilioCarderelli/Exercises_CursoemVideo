# Digite um salário e calcule um aumento baseado no valor do salário,
# sendo: 15% para menor que 2000 e 10% para maior.

salario = float(input('Qual é o seu salário? R$'))
if salario > 2000:
    print('Com um salário de R${}, e um aumento de {}%, o novo salário será: {}'
          .format(salario, 10, salario + (salario * 10/100)))
if salario <= 2000:
    print('Com um salário de R${}, e um aumento de {}%, o novo salário será: {}'
          .format(salario, 15, salario + (salario * 15/100)))
