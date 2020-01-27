#Exe014 - Digite um valor em ºC e converta em ºF.

C = float(input('Qual a temperatura em ºC? '))
F = ((9 * C) / 5) + 32
# F = 9 * C / 5 + 32
print('{}ºC é equivalente á {}ºF'.format(C, F))
