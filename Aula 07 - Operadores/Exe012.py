# Exe012 - Digite um preço e calcule seu desconto com n%.

valor = float(input('Qual é o preço do produto? R$'))
desconto = float(input('Quanto é o desconto em (%)? '))
pcd = valor * (1 - desconto / 100)

print('O valor de R${} com o desconto de {}% é igual a R${}'.format(valor, desconto, pcd))
