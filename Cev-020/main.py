from random import shuffle 

D1=str(input('Digite o nome do primeiro aluno'))
D2=str(input('Digite o nome do segundo aluno'))
D3=str(input('Digite o nome do terceiro aluno'))
D4=str(input('Digite o nome do quarto aluno'))
kc=[]
kc.append(D1)
kc.append(D2)
kc.append(D3)
kc.append(D4)
shuffle(kc)
print(kc)