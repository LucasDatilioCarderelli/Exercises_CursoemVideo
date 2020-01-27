# Exe077 - Crie uma tupla com varias palavras e mostre as vogais.

palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro', 'profissional',)
for n in palavras:
    print(f'\nNa palavra {n.upper():.<13} temos: ', end='')
    for letra in n:
        if letra in 'aeiou':
            print(f'{letra}', end=' ')
