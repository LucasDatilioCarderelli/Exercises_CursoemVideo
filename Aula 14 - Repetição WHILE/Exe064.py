# Exe064 - Digite varios números e some entre eles até digitar 999 para parar.

print('Soma de valores\nDigite 999 para parar e somar.')
num = 0
soma = 0
cont = 0
# num = soma = cont = 0
while num != 999:
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
print('Foram digitados {} números e a soma entre eles é {}'.format(cont - 1, soma - 999))
# num = int(input('Digite um número: '))
# while num != 0:
#     num = int(input('Digite um número: '))
#     soma += num
#     cont += 1
# print('Foram digitados {} números e a soma entre eles é {}'.format(cont, soma))
