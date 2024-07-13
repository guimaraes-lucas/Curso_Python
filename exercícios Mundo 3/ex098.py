"""
    Faça um programa que tenha uma FUNÇÃO chamada CONTADOR(), que receba TRÊS PARÂMETROS: INÍCIO, FIM e PASSO. Seu
programa tem que realizar TRÊS CONTAGENS através da função criada:
    A) De 1 até 10, de 1 em 1
    B) De 10 até 0, de 2 em 2
    C) Uma contagem PERSONALIZADA
"""
from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    print(f'Realizando a contagem de {inicio} a {fim}, de {passo} em {passo}')

    cont = inicio
    if inicio < fim:
        while cont <= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += passo
    elif inicio > fim:
        while cont >= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= passo
    print('FIM')


contador(1, 10, 1)
print()

contador(10, 0, 2)
print()

print('Agora é a sua vez de Personalizar a Contagem: ')
print()

inicial = int(input('Início: '))
final = int(input('Fim: '))
contagem = int(input('Passo: '))

contador(inicial, final, contagem)
