# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial

num = int(input('Digite o número para calcular seu fatorial: '))

contador = num
fatorial = factorial(num)

print(f'Calculando {num}! = ', end='')

while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    contador -= 1

print(fatorial)
