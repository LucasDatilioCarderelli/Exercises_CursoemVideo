# Exe024 - Digite o nome da cidade e verifique se começa com Santo.

Cidade = str(input('Onde você nasceu? ').strip())
LCidade = Cidade.lower()
# print(LCidade.find('santo'))
print('Começa com Santo?', LCidade[:5] == 'santo')
