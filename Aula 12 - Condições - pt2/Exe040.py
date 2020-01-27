# Exe040 - Digite duas notas e tire a media, descubra se:
#          Está reprovado(<5), recuperação(=5<7), aprovado(=>7)

num1 = float(input('Digite a 1º nota: '))
num2 = float(input('Digite a 2º nota: '))
media = (num1 + num2) / 2
if 0 < num1 > 10 or 0 < num2 > 10:
    print('Erro: OBRIGATORIO Nota entre 0 e 10!')
    exit()
elif media < 5:
    print('REPROVADO!')
elif media < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
print('A media é {:.1f}'.format(media))
