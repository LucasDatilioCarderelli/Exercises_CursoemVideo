# Exe005 - Digite um número inteiro e tenha seu sucessor e antecessor.

num = int(input('Digite um número: '))
Suce = num + 1
Ante = num - 1
print('O antecessor é {}{}{}, o número é {} e o sucessor é {}{}{}'
      .format('\033[32m', Ante, '\033[m', num, '\033[31m', Suce, '\033[m'))
