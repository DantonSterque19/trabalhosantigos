#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

H=float(input('Digite o valor da casa'))
Sal=float(input('Digite o seu salario'))
An=int(input('DIgite em quantos anos a casa será paga'))
Qua= H / An*12
Mul= Sal*0.30
TAn=H/(An*12)
if Mul<TAn:
  print('Para pagar esta casa em {} anos são necessarios R${:.2f},sabendo que o limite do seu salario (Apenas 30% do mesmo) permite pagar uma mensalidade de até R${:.2f}... Você terá o empréstimo negado, recomenda-se procurar outro imovél...'.format(An,TAn,Mul))
elif Mul>=TAn:
  print('Para pagar esta casa em {} anos são necessarios R${:.2f},sabendo que o limite do seu salario (Apenas 30% do mesmo) permite pagar uma mensalidade de até R${:.2f}... Você terá o empréstimo permitido :) '.format(An,TAn,Mul))
