# Exe027 - Digite seu nome e analise.

n = str(input('Qual é o seu nome: ').strip())
nome = n.split()
print(nome[0])
print(nome[len(nome)-1])
