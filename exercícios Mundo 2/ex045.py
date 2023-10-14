# Crie um programa que faça o computador jogar JOKENPÔ com você.

from random import choice
from time import sleep

jogadas = ('pedra', 'papel', 'tesoura')

print('[ 0 ] Pedra')
print('[ 1 ] Papel')
print('[ 2 ] Tesoura')

escolhaComputador = choice(jogadas)
escolhaJogador = int(input('Escolha sua jogada: '))

if escolhaJogador == 0:
    escolhaJogador = jogadas[0]
elif escolhaJogador == 1:
    escolhaJogador = jogadas[1]
elif escolhaJogador == 2:
    escolhaJogador = jogadas[2]

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')

print('-=-' * 20)
print('O computador escolheu {}'.format(escolhaComputador))
print('Você escolheu {}'.format(escolhaJogador))
print('-=-' * 20)

if (escolhaJogador == jogadas[0] and escolhaComputador == jogadas[0] or
        escolhaJogador == jogadas[1] and escolhaComputador == jogadas[1] or
        escolhaJogador == jogadas[2] and escolhaComputador == jogadas[2]):
    print('\033[1:37mEmpate\033[m')
elif (escolhaJogador == jogadas[0] and escolhaComputador == jogadas[2] or
      escolhaJogador == jogadas[1] and escolhaComputador == jogadas[0] or
      escolhaJogador == jogadas[2] and escolhaComputador == jogadas[1]):
    print('\033[1:32mVocê venceu!!!\033[m')
elif (escolhaJogador == jogadas[0] and escolhaComputador == jogadas[1] or
      escolhaJogador == jogadas[1] and escolhaComputador == jogadas[2] or
      escolhaJogador == jogadas[2] and escolhaComputador == jogadas[0]):
    print('\033[1:31mVocê perdeu!!!\033[m')
