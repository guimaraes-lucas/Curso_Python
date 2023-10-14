"""
    Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
import random
from time import sleep

print('=-=' * 20)
print('Adivinhe o número que estou pensando!!')
print('=-=' * 20)

n = int(input('Que número você acha que é?: '))
print('Processando...')
sleep(2)
computador = [0, 1, 2, 3, 4, 5]
r = random.choice(computador)       # random.randint(0, 5)

if n == r:
    print('Parabéns!! Você acertou !!!')
else:
    print('Desculpe, você errou!. Eu pensei no número {} não no número {}'.format(r, n))
