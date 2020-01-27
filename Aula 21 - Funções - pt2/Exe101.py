# Exe101 - Crie uma funcao 'voto()' recebendo parametro 'Ano de nascimento' e retornando:
# Voto: 'Negado', 'Opcional', 'Obrigatorio'.


def voto(ano):
    from datetime import date
    actual_year = date.today().year
    age = actual_year - ano
    if age < 16:
        return print(f'Quem tem {age} anos o voto é: NEGADO')
    elif 18 < age < 65:
        return print(f'Quem tem {age} anos o voto é: OBRIGATORIO')
    else:
        return print(f'Quem tem {age} anos o voto é: OPCIONAL')


born_year = int(input('Ano de nascimento: '))
voto(born_year)
