# Exe053 - Digite uma frase e descubra se é um palindromo.

frase = str(input('Digite uma frase: ').replace(' ', '').lower())
# .strip
# palavras = frase.split
# junto = ''.join(palavras)
inverso = ''
# inverso = frase[::-1]
print(inverso)
for c in range(len(frase) - 1, -1, -1):
    inverso += frase[c]
print(frase, inverso)
if frase == inverso:
    print('É um Palindromo')
else:
    print('Não é um palindromo')
