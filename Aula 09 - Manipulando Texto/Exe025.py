# Exe025 - Digite um nome e verifique se tem 'Silva'.

nome = str(input('Seu nome tem Silva?\nDigite seu nome: ')).strip()
Lnome = nome.lower()
print('Você, {}, tem Silva no nome? {}'.format(nome, 'silva' in Lnome))
