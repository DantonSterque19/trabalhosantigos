from random import randint
pa=randint(0,5)
pe=int(input('Digite um numero'))
if pa==pe:
  print('Você ganhou da maquina')
elif pa!=pe:
  print('Você perdeu da maquina')