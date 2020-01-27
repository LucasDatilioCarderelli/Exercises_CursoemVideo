# Exe031 - Digite a distancia da viagem, sendo que (até 200Km, valor igual a R$0,50 por Km;
# se maior de 200km, valor igual a R$0,45 por Km).

distancia = float(input('Quantos a distancia da viagem em Km? '))
# preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
maiorduz = 0.50
menorduz = 0.45
if distancia >= 200:
    print('Numa viagem de {}Km, o custo será de R${:.2f}\nCada Km custou R${:.2f}'
          .format(distancia, distancia * maiorduz, maiorduz))
else:
    print('Numa viagem de {}Km, o custo será de R${:.2f}\nCada Km custou R${:.2f}'
          .format(distancia, distancia * menorduz, menorduz))

exit()