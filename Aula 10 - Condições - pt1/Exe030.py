# Exe030 - Digite um número e descubra se ele é par ou impar.

num = int(input('Digite um número inteiro qualquer: '))
par = int(num / 2) * 2
impar = float(num / 2) * 2
# resultado = num % 2

if par == impar:
    if par == 0:
        print('0 não é par nem impar')
    else:
        print('Esse número é par')
else:
    print('Esse numero é impar')
