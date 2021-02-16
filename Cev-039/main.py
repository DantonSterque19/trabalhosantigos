#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
Pap=int(input('Digite o seu ano de nascimento'))
ppa=2019
t=ppa-Pap
if  t == 18 :
  print('Você deverá fazer seu alistamento este ano')
elif t > 18:
  print('Você deverá fazer o seu alistamento o mais rapido possivel,pois você passou {} anos dos 18 anos'.format(t-18))  
elif t < 18 :
  print('Você ainda não deverá fazer seu alistamento militar')