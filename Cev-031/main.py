Dis=float(input('Digite a distancia do trajeto a ser percorrido(em Km)'))
if Dis <200:
  pas=Dis*0.50
elif Dis>200:
  pas=Dis*0.45
print('O total a ser pago na passagem é de R${:.2f}'.format(pas))