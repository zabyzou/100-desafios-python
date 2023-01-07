from math import tan, radians, sin, cos
angulo = float(input('Digite o angulo que você deseja:'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O angulo de {} tem o seno de {:.2f}'.format(angulo, seno))
print('O angulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))
print('O angulo de {} tem a tangente de {:.2f}'.format(angulo, tangente))

