# Exe042 - Digite três retas, verique se forma um triangulo e qual tipo.

a = int(input('Primeiro segmento (cm): '))
b = int(input('Segundo segmento (cm): '))
c = int(input('Terceiro segmento (cm(: '))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print('É possivel formar um triangulo: ', end='')
    if a == b == c:
        print('EQUILATERO')
    elif a == b or a == c or b == c:
        print('ISÓSELES')
    elif a != b != c != a:
        print('ESCALENO')
else:
    print('NÃO é possivel formar um triangulo!')
    exit()
