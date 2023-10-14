# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math

ang = float(input('Insira o ângulo: '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O seno é: {:.2f}'.format(sen))
print('O cosseno é: {:.2f}'.format(cos))
print('O tangente é: {:.2f}'.format(tan))
