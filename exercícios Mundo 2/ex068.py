"""
    Faça um programa que jogue PAR ou ÍMPAR com o computador. O jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint

contagem = 0

print('-=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=-' * 20)

while True:
    jogador = int(input('Escolha um número: '))
    computador = randint(0, 11)

    escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    print('-'*30)
    resultado = (jogador + computador) % 2

    if escolha == 'P':
        if resultado == 0:
            contagem += 1
            print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {jogador + computador} DEU PAR')
            print('-' * 30)
            print('Você VENCEU !!!')
            print('Vamos jogar novamente...')
        else:
            print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {jogador + computador} DEU ÍMPAR')
            print('-' * 30)
            print('Você PERDEU !!!')
            break
    elif escolha == 'I':
        if resultado == 1:
            contagem += 1
            print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {jogador + computador} DEU Ímpar')
            print('-' * 30)
            print('Você VENCEU !!!')
            print('Vamos jogar novamente...')
        else:
            print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {jogador + computador} DEU PAR')
            print('-' * 30)
            print('Você PERDEU !!!')
            break
print('-=-'*20)
print(f'GAME OVER ! Você venceu {contagem} vezes.')
