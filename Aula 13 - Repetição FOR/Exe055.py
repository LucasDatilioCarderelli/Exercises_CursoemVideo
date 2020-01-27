# Exe055 - Digite o peso de 5 pessoas e selecione o maior e menor.

maior = 0
menor = 0
for n in range(1, 5+1):
    peso = float(input('Qual o peso da {}ª pessoa: '.format(n)))
    if n == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(maior, menor)
