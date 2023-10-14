# Crie um programa que leia um número Real qualquer pelo teclado é mostre na tela a sua porção inteira.

from math import trunc

num = float(input('Insira um valor a ser arrendodado: '))
a = trunc(num)

print('O número escolhido é {}, arrendodando ficaria {}'.format(num, a))
