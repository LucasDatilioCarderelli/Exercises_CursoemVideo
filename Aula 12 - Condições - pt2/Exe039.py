# Exe039 - Digite o ano de nascimento e descubra se,
# já passou do tempo, hora de alistar ou se ainda vai se alistar e quanto tempo falta ou passou.

from datetime import date

nascimento = int(input('Qual o ano de nascimento: '))

print('Quem nasceu em {} tem em 2019, {}anos'
      .format(nascimento, date.today().year - nascimento))

if date.today().year - nascimento == 18:
    print('Está na hora de se alistar')
elif date.today().year - nascimento > 18:
    print('O perido de alistamento foi há {} anos.'
          .format((date.today().year - nascimento) - 18))
elif date.today().year - nascimento < 18:
    print('Ainda falta {} anos para se alistar.'.format(18 - (date.today().year - nascimento)))

