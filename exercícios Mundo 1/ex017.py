#  Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule
# e mostre o comprimento da hipotenusa.
from math import sqrt

co = float(input('Qual o tamanho do seu Cateto Oposto?: '))
ca = float(input('Qual o tamanho do seu Cateto Adjacente?: '))

h = sqrt((co ** 2) + (ca ** 2))     # math.hypot(x, y)

print('Sua hipotenusa é {:.2f}'.format(h))
