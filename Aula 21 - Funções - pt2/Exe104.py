# Exe104: Crie uma função leiaInt() semelhante 'a função input(),
# fazendo a validação para aceitar apenas um valor numérico.


def leiaint(msg):
    """
    -> Function to read a int number.
    :param msg: Campo para acolher um número
    :return: Retorna valor inteiro.
    """
    while True:
        num = input(msg)
        if not num.isnumeric():
            print('\033[1;031mVocê não digitou um número...\033[m')
        else:
            num = int(num)
            break
    return num


# Principal
n = leiaint('Digite um Número: ')
print(f'Você acabou de digitar o numéro {n}')