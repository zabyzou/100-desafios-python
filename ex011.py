largura = float(input('Largura da parede:'))
altura = float(input('Altura da parede:'))
area = largura * altura
print('A sua parede tem uma dimensão de {}x{} é uma área de {}m²'.format(largura, altura, area))
tinta = area / 2
print('Você vai precisar de {} litros de tinta para pintar a parede'.format(tinta))

