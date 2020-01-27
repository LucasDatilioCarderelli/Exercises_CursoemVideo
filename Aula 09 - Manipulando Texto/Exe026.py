# Exe026 - Digite algo e analise quantas vezes aparece a letra A,
# a posição do primeiro A e do ultimo A.

frase = str(input('Digite algo: ').strip())
frasel = frase.lower()
print('A letra "A" aparece {} vezes'.format(frasel.count('a')))
print('A primeira letra "A" aparece na posição {}'.format(frasel.find('a')+1))
print('A ultima letra "A" aparece na posição {}'. format(frasel.rfind('a')+1))
