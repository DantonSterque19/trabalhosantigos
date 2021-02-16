print('=-'*10,'Condição de existencia de triangulos','=-'*2)
a=float(input('Digite a primeira medida (A)'))
b=float(input('Digite a segunda medida (B)'))
c=float(input('Digite a terceira medida (C)'))
#| b - c | < a < b + c
#| a - c | < b < a + c
#| a - b | < c < a + b
if a<b+c:
  print('Formam um triangulo')
elif b<a+c:
  print('Formam um triangulo')
elif c<b+a:
  print('Formam um triangulo')
elif a>b+c:
  print('Não formam um triangulo')
elif b>a+c:
  print('Não formam um triangulo')
elif c>a+b:
  print('Não formam um triangulo')