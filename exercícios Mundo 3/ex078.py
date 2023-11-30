"""
    Faça um programa que leia 5 VALORES NUMÉRICOS e quarde-os em uma LISTA. No final, mostre qual foi o MAIOR e o MENOR
valor digitado e as suas respectivas POSIÇÕES na LISTA.
"""

lista = []

for num in range(0, 5):
    lista.append(int(input(f'Insira o número da posição {num}: ')))
maior = max(lista)
menor = min(lista)

print('_'*30)

print(f'O maior valor foi {max(lista)} e sua posição é ', end='')
for indice, valor in enumerate(lista):
    if valor == maior:
        print(f'{indice}... ', end='')

print()

print(f'O menor valor foi {min(lista)} e sua posição é ', end='')
for indice, valor in enumerate(lista):
    if valor == menor:
        print(f'{indice}... ', end='')