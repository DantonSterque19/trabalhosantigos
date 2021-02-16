km=float(input('Digite quantos Km rodados?'))
d=int(input('A quantos dias você está com ele?'))
sad=d*60
sada=km*0.15
tol=sad+sada
print('O total a pagar é de R${:.2f}'.format(tol))