from math import sin, cos,tan,radians
ang=int(input('Digite um angulo'))
sina=radians(sin(ang))
print('O seno de {} é {:.2f}, o cosseno é {:.2f} e a tangente é de {:.2f}'.format(ang,sina,radians(cos(ang)),radians(tan(ang))))