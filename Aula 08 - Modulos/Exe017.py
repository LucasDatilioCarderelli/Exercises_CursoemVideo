# Exe017 - Digite o valor dos catetos e calcule a hipotenusa.

Co = float(input('Digite o valor do Cateto oposto: '))
Ca = float(input('Digite o valor do Cateto adjacente: '))
Hi = (Ca**2 + Co**2) ** (1/2)
print()
print('O valor de hipotenusa é {:.2f}'.format(Hi))
# import math
# Hip = math.hypot(Co, Ca)
