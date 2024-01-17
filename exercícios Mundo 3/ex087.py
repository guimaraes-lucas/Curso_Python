"""
    Aprimore o DESAFIO ANTERIOR, mostrando no final:
        A) A SOMA de todos os VALORES PARES digitados.
        B) A SOMA dos valores da TERCEIRA COLUNA.
        C) O MAIOR valor da SEGUNDA LINHA.
"""

matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
somaPar = somaCol3 = maiorLin2 = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}, {coluna}]: '))

        # Soma dos Valores pares
        if matriz[linha][coluna] % 2 == 0:
            somaPar += matriz[linha][coluna]

        # Soma dos valores da terceira coluna
        somaCol3 += matriz[linha][2]

        # Maior valor da segunda linha
        if matriz[1][coluna] == 0:
            maiorLin2 = matriz[1][coluna]
        elif matriz[1][coluna] > maiorLin2:
            maiorLin2 = matriz[1][coluna]

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

print(f'A soma total dos valores pares da matriz é: {somaPar}')
print(f'A soma da terceira coluna da matriz é: {somaCol3}')
print(f'O maior valor da segunda linha é: {maiorLin2}')
