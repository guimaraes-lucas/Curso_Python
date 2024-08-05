"""
    Faça um programa que tenha uma LISTA chamada NÚMEROS e duas FUNÇÕES chamadas SORTEIA() e SOMAPAR(). A primeira
função vai sortear 5 NÚMEROS e vai colocá-los dentro da lista e a segunda função vai mostrar a SOMA entre todos os
valores PARES sorteados pela função anterior.
"""
from random import randint


def sorteia(lista):
    cont = 0
    while cont < 5:
        lista.append(randint(1, 10))
        cont += 1
    print(f'Sorteando 5 valores da lista: {lista} PRONTO!')

def somaPar(lista):
    total = 0
    for valor in lista:
        if valor % 2 == 0:
            total += valor
    print(f'Somando os valores pares de {lista}: {total}')


numeros = []

sorteia(numeros)
somaPar(numeros)