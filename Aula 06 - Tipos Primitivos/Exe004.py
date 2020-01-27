# Exe004 - Digite algo e tenha seus tipos primitivos.

a = input('\033[1;032mDigite algo\033[m: ')
print('O tipo primitivo é: ', type(a))
print('Só tem espaço? ', a.isspace())
print('É um numero? ', a.isnumeric())
print('Está em minusculo? ', a.islower())
print('Está em maisculo? ', a.isupper())
print('A primeira letra está em maisculo? ', a.istitle())
