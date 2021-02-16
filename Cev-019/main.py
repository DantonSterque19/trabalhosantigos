from random import randint, shuffle
D=str(input('Digite o primeiro nome'))
D2=str(input('Digite o segundo nome'))
D3=str(input('Digite o terceiro nome'))
D4=str(input('Digite o quarto nome'))
Nom=[D,D2,D3,D4]
print('A pessoa escolhida foi {}'.format(Nom[randint(0,3)]))
print(shuffle(Nom,6))