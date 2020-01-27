# Exe097 - Crie uma função com parametro de mensagem variavel.


def escreva(msg):
    print('-' * len(msg))
    print(msg)
    print('-' * len(msg))


escreva(f'{"Olá Mundo!":^30}')
escreva(f'{"Curso em Vídeo":^30}')
escreva(f'{"Python":^30}')
