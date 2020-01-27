# Exe065 - Digite varios números, pergunte [S/N] para continuar e tenha:
# Media, maior e menor.

num = soma = cont = media = 0
parada = ''
maior = 0
menor = 0
while parada != 'N':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    media = soma / cont
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    parada = str(input('Deseja Continuar? [ S/N ]: ').upper().strip()[0])
    while parada != 'S' and parada != 'N':
        print('Opção invalida')
        parada = str(input('Deseja Continuar? [ S/N ]: ').upper())
print('Foram digitados {} números.\nA soma  é: {}\nA média é: {}\nO maior é: {}\nO menor é: {}'
      .format(cont, soma, media, maior, menor))
