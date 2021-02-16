D=str(input('Digite uma frase'))
print('A letra a aparece {} vezes'.format(D.count('A')+1))
print('A letra a aparece primeiro em {}'.format(D.find('A')+1))
print('A letra a aparece,pela ultima vez em {}'.format(D.rfind('A')+1))