from math import floor, sqrt
co = float(input('Valor do cateto oposto:'))
ca = float(input('Valor do cateto adjacente'))
hipotenusa = sqrt(co ** 2 + ca ** 2)
print('O valor da hipotenusa é {}'.format(hipotenusa))
