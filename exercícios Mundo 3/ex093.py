"""
    Crie um programa que gerencie o aproveitamento de um JOGADOR DE FUTEBOL. O programa vai ler o NOME DO JOGADOR e
QUANTAS PARTIDAS ele jogou. Depois vai ler a QUANTIDADE DE GOLS feitos em CADA PARTIDA. No final, tudo isso será guardado
em um DICIONÁRIO incluindo o TOTAL DE GOLS feitos durante o campeonato
"""

jogador = {'nome': str(input('Nome do jogador: ')),
           'jogos': int(input('De quantos jogos ele participou?: ')),
           'gols': []}
total = 0
for x in range(0, jogador['jogos']):
    gol = int(input(f'  Quantos gols no jogo {x+1}? '))
    total += gol
    jogador['gols'].append(gol)
    jogador['total'] = total

print('==='*30)
print(jogador)
print('==='*30)

for item, valor in jogador.items():
    print(f'O campo {item} tem o valor {valor}')

print('==='*30)

print(f'O jogador {jogador["nome"]} jogou {jogador["jogos"]} partidas.')
for indice, valor in enumerate(jogador['gols']):
    print(f'    => Na partida {indice+1}, fez {valor} gols')
print(f'Foi um total de {jogador["total"]} gols.')

"""
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
for c in range(0, tot):
    partidas.append(int(input(f'    Quantos gols na partida {c}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
"""
