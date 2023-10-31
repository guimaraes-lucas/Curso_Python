# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão, usando
# a estrutura while

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Qual a razão?: '))

contagem = 0

while contagem < 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    contagem += 1
print('ACABOU')
