Vel=float(input('Digite a velocidade do carro'))
if Vel>80:
  l=Vel-80
  print('Infelismente,você passou {}Km do limite,portanto terá que pagar uma multa de R${}'.format(Vel-80),(l*7))