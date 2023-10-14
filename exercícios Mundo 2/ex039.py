"""
    Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele 'ainda vai se
alistar' ao serviço militar, se é a 'hora de se alistar' ou se já 'passou do tempo' do alistamento. Seu programa também
deverá mostrar o tempo que falta ou que passou do prazo.
"""
import datetime

ano = int(input('Qual o ano que você nasceu?: '))
anoAtual = datetime.date.today().year
idade = anoAtual - ano

if idade < 18:
    print('Você tem {} anos e completará 18 anos em {}'.format(idade, (18 - idade) + anoAtual))
    print('Em breve você poderá se alistar!!!')
elif idade == 18:
    print('Você possui {} anos!'.format(idade))
    print('Vá logo se alistar!!!')
elif idade > 18:
    print('Você completou 18 anos em {}'.format((18 - idade) + anoAtual))
    print('Já deveria ter se alistado faz {} anos'.format(idade - 18))
