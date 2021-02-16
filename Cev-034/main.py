Sal=float(input('Digite o seu salario'))
if Sal > 1250:
  au=Sal*0.10
  print('O aumento será de R${:.2f}, no final, você ganhará R${:.2f}'.format(au,Sal+au))
elif Sal <1250:
  au=Sal*0.15
  print('O aumento será de R${:.2f}, no final, você ganhará R${:.2f}'.format(au,Sal+au))