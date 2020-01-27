# Exe032 - Digite um ano e descubra se ele é bissexto.

ano = int(input('Digite um ano,  digite 0 para o ano atual: '))
from datetime import date
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
