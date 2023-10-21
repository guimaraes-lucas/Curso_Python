# Desenvolva um programa que leia SEIS NÚMEROS INTEIROS e mostre a soma daqueles que forem pares. Se o valor digitado
# for ímpar, desconsidere-o.

total = 0

for c in range(1, 7):
    num = int(input('Digite o {}° número: '.format(c)))
    if num % 2 == 0:
        total = total + num
gustavoprint(total)
