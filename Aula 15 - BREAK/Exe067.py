# Exe067 - Tenha a tabuada de um número até digitar um valor negativo.

while True:
    print('{} TABUADA {}'.format('*' * 16, '*' * 16))
    num = int(input('Digite um número para ver sua tabuada: '))
    if num < 0:
        break
    for c in range(1, 10+1):
        print(f'{num:2.0f} x {c:2.0f} = {num*c:3.0f}')
print('{} FINALIZADO {}'.format('*' * 15, '*' * 15))

