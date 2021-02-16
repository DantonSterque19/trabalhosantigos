#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes
#| b - c | < a < b + c
#| a - c | < b < a + c
#| a - b | < c < a + b
a=float(input('Digite o numero do lado a'))
b=float(input('Digite o numero do lado b'))
c=float(input('Digite o numero do lado c'))
if (b - c) < a < b + c:
  print('Este triangulo exitste')
elif  (a - c) < b < a + c:
 print('Existe um triangulo ')
elif (a - b) < c < a + b:
  print('Existe um triangulo')
