# Exe015 - Calcule o aluguel de um carro, sendo R$60,00/Dia e R$0,15/Km.

dias = int(input('Quantos dias o carro foi alugado? '))
Km = float(input('Quantos Km foi percorrido? '))
valor = (dias * 60) + (Km * 0.15)
print('O carro alugado por {}dias com {}Km rodados custa R${}'.format(dias, Km, valor))
