#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO

P1=float(input('Digite a primeira nota'))
P2=float(input('Digite a segunda nota'))
Pm=(P1+P2)/2
if Pm > 7 :
  print('Você foi aprovado')
elif Pm<5:
  print('Você foi reprovado')
elif 5<= Pm <6.9 :
  print('Você está de recuperação')
  print(Pm)