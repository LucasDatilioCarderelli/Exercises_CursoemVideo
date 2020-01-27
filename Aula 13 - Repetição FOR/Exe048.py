# Exe048 - Some os numeros multiplos de 3 e impares entre 0 e 500.
s = 0
c = 0
for n in range(0, 500, 3):
    if n % 2 != 0:
        s = s + n
        # s += c
        c = c + 1
print(s, 'é a soma de', c, 'números')
