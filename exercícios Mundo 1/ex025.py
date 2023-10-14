# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Qual o seu nome?: ')).strip()
encontrar = 'silva' in nome.lower()

print('Seu nome contém Silva?: {}'.format(encontrar))
