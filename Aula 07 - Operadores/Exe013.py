# Exe013 - Digite um salário e calcule seu aumento em %.

salario = float(input('Qual é o salário? R$'))
aumento = float(input('De quanto é o aumento? R$'))
sca = salario + (salario * aumento / 100)
print('O salário de R${} com um aumento de {}% é de R${}'.format(salario, aumento, sca))
