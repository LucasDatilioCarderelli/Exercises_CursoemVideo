# Exe043 - Calculo de IMC (Indice de Massa Corporal),
# sendo: abaixo do peso (<18), peso ideal (18:25), sobrepeso(25:30),
# obesidade(30:40), obesidade mórbida(40>).

peso = float(input('Digite PESO (Kg): '))
altura = float(input('Digite Altura (cm): '))
altura = altura / 100
IMC = peso / (altura**2)
print('IMC = {:.0f}'.format(IMC))
if IMC < 18:
    print('Abaixo do peso.')
elif 18 <= IMC <= 25:
    print('Peso ideal.')
elif 25 < IMC <= 30:
    print('Sobrepeso.')
elif 30 < IMC <= 40:
    print('Obesidade')
else:
    print('Obesidade móbida')
