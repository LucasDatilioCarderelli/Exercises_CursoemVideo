# Exe054 - Digite 7 anos de nascimento e analise quem são maiores de idade.

cm = 0
cn = 0
from datetime import date
for n in range(1, 7+1):
    nascimento = int(input('Qual é o {}ª ano de nascimento?: '.format(n)))
    idade = date.today().year - nascimento
    if idade >= 18:
        cm += 1
    else:
        cn += 1
print('Temos {} maiores de idade, e\nTemos {} menores de idade.'.format(cm, cn))