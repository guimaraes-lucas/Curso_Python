#   Faça um programa que calcule a soma entre todos os NÚMEROS ÍMPARES que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.
soma = 0
cont = 0

for impares in range(1, 501, 2):
    if impares % 3 == 0:
        soma += impares
        cont += 1
        print('Ao todo existem {} números múltiplos de 3 e a soma deles é {}'.format(cont, soma))
