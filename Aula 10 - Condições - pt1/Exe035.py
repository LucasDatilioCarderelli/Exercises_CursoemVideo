# Exe035 - Digite 3 valores de reta e verifique se forma um triangulo.
# Se a soma das medidas de dois deles é sempre maior que a medida do terceiro, então,
# eles podem formar um triângulo.

a = float(input('Digite uma medida: '))
b = float(input('Digite outra medida: '))
c = float(input('Digite uma outra medida: '))

ab = a + b
ac = a + c
bc = b + c

maior = a
if b > a and b > c:
    maior = b
else:
    maior = c

if c < ab and ac and bc:
    print('É possivel formar um triangulo!')
else:
    print('Não é possivel')

# if ab > c and ac > b and bc > a:
#     print('É possivel formar um triangulo!')
# else:
#     print('Não é possivel')
