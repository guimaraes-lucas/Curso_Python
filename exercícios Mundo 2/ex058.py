"""
    Melhore o jogo so DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites forem necessários para vencer.
"""

import random
from time import sleep

print('Sou o seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Consegue adivinhar qual foi?')

computador = random.randrange(0, 10)
jogador = int(input('Qual é o seu palpite? '))
tentativas = 1

while computador != jogador:
    if jogador > computador:
        print('Menos...')
        jogador = int(input('Qual é o seu palpite? '))
    else:
        print('Mais...')
        jogador = int(input('Qual é o seu palpite? '))

    tentativas += 1
print('Acertou em {} tentativas. Parabéns!!'.format(tentativas))
