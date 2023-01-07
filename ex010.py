real = float(input('Qual o saldo disponível em sua carteira? R$'))
dolar = real / 5.43
euro = real / 5.77
libraesterlina = real / 6.56
print('Com o seu saldo atual você consegue comprar:')
print('US${:.2f}.'.format(dolar))
print('€{:.2f}'.format(euro))
print('£{:.2f}'.format(libraesterlina))


