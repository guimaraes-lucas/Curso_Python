# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

x = int(input('Digite um valor: '))
d = x * 2
t = x * 3
r = x ** (1/2)

print('O dobro de {} é {}.\nO triplo de {} é {}.\nA raiz de {} é {} '.format(x, d, x, t, x, r))
