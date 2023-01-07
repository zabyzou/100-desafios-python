medida = float(input('Uma distancia em mêtros:'))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
print('Medida em centimetros:{} cm'.format(cm))
print('Medida em milimetros:{} mm'.format(mm))
print('Medida em quilometros:{} km'.format(km))
print('Medida em hectometros:{} hm'.format(hm))
print('Medida em decametros:{} dam'.format(dam))
print('Medida em decimetros:{} dm'.format(dm))


