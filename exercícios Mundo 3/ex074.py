"""
    Crie um programa que vai gerar CINCO NÚMEROS ALEATÓRIOS e colocar em uma TUPLA. Depois disso, mostre a LISTAGEM
DE NÚMEROS gerados e tambem indique o MENOR e o MAIOR valor que estão na tupla.
"""
from random import randint

nums = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10),)

print(f'Os valores sorteados foram: {nums}')
print(f'O maior valor sorteado foi: {max(nums)}')
print(f'O menor valor sorteado foi: {min(nums)}')


