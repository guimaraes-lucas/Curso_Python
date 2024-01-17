"""
    Crie um programa que crie uma MATRIZ de DIMENSÃO 3X3 e preencha com valores lidos pelo teclado. No final, mostre a
MATRIZ na tela, com a formatação correta.
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor da posição [{linha}, {coluna}]: '))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()