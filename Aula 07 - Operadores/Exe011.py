# Exe011 - Digite dois valores em metros e descubra quantos litros de tinta é nescessario.
# (1m^2 = 2L)

l = float(input('Digite a largura em (m): '))
h = float(input('Digite a altura em (m): '))
a = l * h
L = a / 2

print('Numa parede  de {}m por {}m tem uma área de {}m'.format(l, h, a))
print('Numa área de {}m utilizará {}L de tinta'.format(a, L))
