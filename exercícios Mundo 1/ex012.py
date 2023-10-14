# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Qual o valor do produto?: '))
d = p * 0.05
v = p - d
# v = p + (p * 5 / 100)
print('Seu produto vale {}R$, com o nosso desconto de 5% ({}R$), seu novo valor é {}R$'.format(p, d, v))
