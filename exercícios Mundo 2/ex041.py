"""
    A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade:

    -Até 9 anos: Mirim              -Até 25 anos: Sênior
    -Até 14 anos: Infantil          -Acima: Master
    -Até 19 anos: Junior
"""

from datetime import date

anoNascimento = int(input('Ano de Nascimento: '))
anoAtual = date.today().year

idade = anoAtual - anoNascimento

if idade <= 9:
    print('Você possui {} anos'.format(idade))
    print('Sua categoria é MIRIM')
elif 10 <= idade <= 14:
    print('Você possui {} anos'.format(idade))
    print('Sua categoria é INFANTIL')
elif 15 <= idade <= 19:
    print('Você possui {} anos'.format(idade))
    print('Sua categoria é JUNIOR')
elif 20 <= idade <= 25:
    print('Você possui {} anos'.format(idade))
    print('Sua categoria é SÊNIOR')
elif idade > 25:
    print('Você possui {} anos'.format(idade))
    print('Sua categoria é MASTER')
