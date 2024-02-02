"""
    Crie um programa onde 4 JOGADORES joguem um DADO e tenham resultados ALEATÓRIOS. Guarde esses resultados em um
DICIONÁRIO. No final, coloque esse dicionário em ORDEM, sabendo que o VENCENDOR tirou o MAIOR NÚMERO no dado.
"""

from random import randint
from operator import itemgetter

jogo = {'jogador1': randint(1,6), 'jogador2': randint(1,6),
        'jogador3': randint(1,6), 'jogador4': randint(1,6)}
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('Valores sorteados: ')
for jogador, ponto in jogo.items():
    print(f'{jogador} tirou {ponto} no dado')

print('-=-'*30)

print('== RANKING DOS JOGADORES ==')
for posicao, resultado in enumerate(ranking):
    print(f'{posicao+1}° lugar: {resultado[0]} com {resultado[1]}')

"""
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6), 
        'jogador2': randint(1,6),
        'jogador3': randint(1,6), 
        'jogador4': randint(1,6)}
ranking = list()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)
"""