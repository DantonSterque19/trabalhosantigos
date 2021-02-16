al=float(input('Digite a altura da parede (em metros)'))
lar=float(input('Digite a largura da parede (em metros)'))
Area=al*lar
tinta=Area/2
print('A area da parede é {}m^2'.format(Area))
print('Serão necessários {:.2f}L de tinta para pintar a parede'.format(tinta))