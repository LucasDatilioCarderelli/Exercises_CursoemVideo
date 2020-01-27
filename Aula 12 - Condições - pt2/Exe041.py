# Exe041 - Digite o ano de nascimento e clasifique-o em que faixa está,
# sendo: mirim(até 9), infantil(até 14), júnior(até 19), sênior(até 25), master(acima 25).

from datetime import date
nasceu = int(input('Em que ano nasceu?: '))
idade = (date.today().year) - nasceu
print('O atleta tem {} anos'.format(idade))
if idade < 9:
    print('Classificação: MIRIM')
elif idade < 14:
    print('Classificação: INFANTIL')
elif idade < 19:
    print('Classificação: JÚNIOR')
elif idade < 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
