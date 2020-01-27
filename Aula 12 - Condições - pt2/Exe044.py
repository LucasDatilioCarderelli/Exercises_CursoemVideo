# Exe044 - Calcule o preço de um produto dependendo da condição de pagamnto,
# sendo: a vista em dinheiro (10% desconto), a vista em cartão (5% desconto),
#        2x no cartão (preço padrão), 3x ou mais(20% de juros simples).
preco = float(input('Qual é o preço do produto em R$: R$'))
forma = int(input('''
DIGITE [ 0 ] para pagamento a vista;
DIGITE [ 1 ] para pagamento a vista no cartão
DIGITE [ 2 ] para pagamento 2x no cartão
DIGITE [ 3 ] para pagamento 3x no cartão
DIGITE AQUI: '''))
if forma != 0 and 1 and 2 and 3:
    print('ERRO: Opção invalida, porfavor repita!')
    exit()
if forma == 3:
    forma = int(input('Será em quantas veses(3x ou mais)?: '))
Dvista = preco - (preco * 10/100)
Cvista = preco - (preco * 5/100)
Doisx = preco
Tresx = preco + (preco * 20/100)
if forma == 0:
    print('O produto será R${} a vista em notas.'.format(Dvista))
elif forma == 1:
    print('O produto será R${} a vista no cartão.'.format(Cvista))
elif forma == 2:
    print('O produto será R${} no total, sendo 2x de R${}.'.format(Doisx, Doisx / 2))
else:
    print('O produto será R${} no total, sendo {}x de R${}.'
          .format(Tresx, forma, Tresx / forma))
