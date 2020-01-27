# Exe059 - Digite dois valores e mostre um menu,
# sendo: [1]somar, [2]multiplicar, [3]maior, [4]novos números e [5]encerrar.
print('\033[7;30mPYTHON CONSOLE\033[m')
encerrar = False
num1 = int(input('Digite o 1º número: '))
num2 = int(input('Digite o 2º número: '))
while not encerrar:
    print()
    menu = int(input('''Oque deseja fazer?:
[1] Somar;
[2] Multiplicar;
[3] Ter o Maior;
[4] Novos Números;
[5] Encerrar;
Digite \033[33mAQUI\033[m: '''))
    if menu == 4:
        print()
        num1 = int(input('Digite o 1º número: '))
        num2 = int(input('Digite o 2º número: '))
    elif menu == 1:
        soma = num1 + num2
        print('\033[1;32m{} + {} = {}\033[m'.format(num1, num2, soma))
    elif menu == 2:
        mult = num1 * num2
        print('\033[1;32m{} x {} = {}\033[m'.format(num1, num2, mult))
    elif menu == 3:
        if num1 > num2:
            print('\033[1;32m{} > {}\033[m'.format(num1, num2))
        elif num1 < num2:
            print('\033[1;32m{} < {}\033[m'.format(num1, num2))
        else:
            print('\033[1;32m{} = {}\033[m'.format(num1, num2))
    elif menu == 5:
        encerrar = True
    if menu != 1 and menu != 2 and menu != 3 and menu != 4 and menu != 5:
        print(''
              '\033[1;31mERROR\033[m: Opção errada, tente novamente.')
print('\033[1;33mPrograma Encerrado\033[m.')