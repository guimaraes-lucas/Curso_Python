# Faça um programa que leia o peso de CINCO PESSOAS. No final, mostre qual foi o MAIOR e o MENOR pesos lidos.

maior = 0
menor = 0

for pessoas in range(1, 6):
    peso = float(input('Insira o peso da {}° pessoa: '.format(pessoas)))
    if pessoas == 1:
        maior = pessoas
        menor = pessoas
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {}Kg e o menor peso foi {}Kg'.format(maior, menor))
