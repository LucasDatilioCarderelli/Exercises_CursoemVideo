# Exe083 - Digite uma expressão e verifique a quantidade de parenteses.

expressão = str(input('Digite uma expressão aritimetica: '))
expressão.strip().split()
if expressão.count('(') == expressão.count(')'):
    print('Expressão valida')
else:
    print('Expressão errada')
# lista = []
# for simb in expressão:
#     if simb == '(':
#         lista.append('(')
#     if simb == ')':
#         if len(lista) > 0:
#             lista.pop()
#         else:
#             lista.append(')')
#             break
# if len(lista) == 0:
#     print('Ok')
# else:
#     print('Error')
