# Exe066 - Digite varios números e some entre eles até digitar 999 para parar.
# Buff 064.

soma = cont = 0
while True:
    num = int(input(f'Digite um número, Digite [999] para Parar: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A Soma dos {cont} números  é {soma}.')
