"""
    Faça um programa que ajude um jogador da MEGA SENA a criar PALPITES. O programa vai perguntar QUANTOS JOGOS serão
gerados e vai sortear 6 NÚMEROS ENTRE 1 e 60 para cada jogo, cadastrando tudo em uma LISTA COMPOSTA.
"""
import random

print('-'*30)
print('JOGA NA MEGA SENA'.center(30))
print('-'*30)

jogos = int(input('Quantos jogos serão sorteados?: '))
jogadas = []
numSorteado = []

print(f'-=-=-= SORTEANDO {jogos} JOGOS =-=-=-')

# Quantos sorteios serão feitos e adicionados à lista jogadas.
for tentativas in range(0, jogos):
    # Adicionar os números sorteados em numSorteado.
    for nums in range(0, 6):
        numSorteado.append(random.randint(1,60))
        numSorteado.sort()
    # Clonando numSorteados para jogadas
    jogadas.append(numSorteado[:])
    numSorteado.clear()

for indice, lista in enumerate(jogadas):
    print(f'Jogo {indice+1}: {lista}')

"""
from random import randint
from time import sleep
lista = list()
jogos = list()
print('-'*30)
print('JOGA NA MEGA SENA'.center(30))
print('-'*30)

quant = int(input('Quantos jogos você quer que eu sorteie?: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print('-=' * 3, f' SORTEANDO {quant} JOGOS ', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {lista}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)
"""