"""
    Aprimore o DESAFIO 093 para que ele funcione com VÁRIOS JOGADORES, incluindo um sistema de visualização de
DETALHES DO APROVEITAMENTO de cada jogador.
"""
jogadores = []

# Adicionando o dicionário Jogador a lista Jogadores
while True:
    jogador = {
        'Nome': str(input('Qual o nome do jogador? ')),
        'Partidas': int(input('De quantos jogos ele participou? ')),
        'Gols': []
    }
    for x in range(0, jogador["Partidas"]):
        gol = int(input(f'Quantos gols ele fez na {x+1}° partida? '))
        jogador["Gols"].append(gol)

    jogadores.append(jogador)
    while True:
        cont = str(input('Deseja continuar? (S/N) ')).upper()[0]
        if cont in 'SN':
            break
        print('Digite somente S ou N.')
    if cont == 'N':
        break

# Exibindo as informações da lista
print('-=-'*30)
print('Cod', end='')
for i in jogador.keys():
    print(f'{i:>15}', end='')
print()
print(f'-'*50)
for pos, item in enumerate(jogadores):
    print(f'{pos:>3}', end='')
    for valor in item.values():
        print(f'{str(valor):>15}', end='')
    print()

# Selecionando o jogador que deseja observar
while True:
    selecao = int(input('Qual Jogador deseja visualizar? (999 para parar) '))
    print()

    if selecao == 999:
        break
    if selecao >= len(jogadores):
        print(f'O código {selecao} não existe em nosso banco de dados.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[selecao]["Nome"]} -- ')
        print()
        for i, v in enumerate(jogadores[selecao]["Gols"]):
            print(f' -No jogo {i+1} ele fez {v} gols.')
    print()
