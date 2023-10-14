# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de desconto.

s = float(input('Qual o salário do funcionário?: '))
am = s * 0.15
ns = s + am
# ns = s + (s * 15 / 100)
input('O salário do funcionário é {}R$, com o aumento de 15%({}R$), seu novo salário é {}R$'.format(s, am, ns))
