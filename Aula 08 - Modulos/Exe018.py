# Exe018 - Digite um angulo e calculo sen, cos, tan.

import math
Ang = float(input('Digite um angulo: '))
ra = math.radians(Ang)

# seno = sin(math.radians(Ang))
# cosceno = cos(math.radians(Ang))
# tangente = tan(math.radians(Ang))

print('O Cosceno é {:.2f} \nO Seno é {:.2f}\n'
      'A Tangente é {:.2f}'.format(math.cos(ra), math.sin(ra), math.tan(ra)))
