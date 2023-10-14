# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar

r = float(input('Quanto dinheiro você têm?: '))
c = r / 4.88

print('Com R$ {:.2f}, você pode comprar US {:.2f}'.format(r, c))
