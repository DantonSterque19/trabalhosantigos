#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER
An=int(input('Digite a idade do atleta'))
if An<=9:
  print('O atleta está classificado como mirim')
elif 9<An<14:
  print('O atleta está classificado como infantil')
elif 14<An<19:
  print('O atleta está classificado como junior')
elif  19<An<25:
  print('O atleta está classificado como sênior')
elif 25<An:
  print('O atleta está classificado como master')