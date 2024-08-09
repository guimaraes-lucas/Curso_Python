"""
    Faça um programa que tenha uma FUNÇÃO chamada FICHA(), que receba dois PARÂMETROS OPCIONAIS: o NOME de um jogador
e quantos GOLS ele marcou. O programa deverá ser capaz de mostrar a FICHA DO JOGADOR, mesmo que algum dado não tenha
sido informado corretamente.
"""


def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


jogador = str(input('Nome do Jogador: '))
gol = str(input('Número de gols: '))

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

if jogador.strip() == '':
    ficha(gols=gol)
else:
    ficha(jogador, gol)

