# Crie um programa que leia o Ano de Nascimento de sete pessoa. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores.

import datetime

anoAtual = datetime.date.today().year
maiores = 0
menores = 0
for pessoas in range(1, 8):

    anoNascimento = int(input('Em que ano nasceu a {}° pessoa?: '.format(pessoas)))
    idade = anoAtual - anoNascimento

    if idade > 18:
        maiores += 1
    else:
        menores += 1

print('Ao todo temos {} pessoas maiores de idade e {} pessoas menores de idade'.format(maiores, menores))
