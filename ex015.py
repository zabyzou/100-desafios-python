day = float(input('Por quantos dias o carro foi alugado?'))
km = float(input('Quantos km o carro andou?'))
day = day * 60
km = km * 0.15
preço = day + km
print('O preço a pagar pelo aluguel do carro é R${:.2f}'.format(preço))

