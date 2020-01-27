# Exe023 - Digite um número (1 á 9999) e mostre: unidade, dezena, centena e milhar.

num = int(input('Digite um número até 9999: '))
# n = str(num)
# print('Unidade: ', n[3])
# print('Dezena : ', n[2])
# print('Centena: ', n[1])
# print('Milhar : ', n[0])

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}\nDezena : {}\nCentena: {}\nMilhar : {}'.format(u, d, c, m))
