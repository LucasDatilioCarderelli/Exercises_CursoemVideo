# Exe008 - Digite uma medida em metros e tenha suas conversões.

metro = float(input('Qual é a medida em metros? '))
decimetro  = metro * 10
centimetro = metro * 100
milimetro  = metro * 1000
kilometro  = metro / 1000
hectametro = metro / 100
decametro  = metro / 10

print('A medida {} equivale a: \n{}km\n{}hec\n{}dac\n{}m\n{}dc\n{}cm''\n{}mm'
      .format(metro, kilometro, hectametro, decametro, metro, decimetro, centimetro, milimetro))
