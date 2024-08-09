"""
    Crie um programa que tenha uma FUNÇÃO chamada VOTO() que vai receber como PARÂMETRO o ANO DE NASCIMENTO de uma
pessoa, RETORNANDO um valor LITERAL indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""
from datetime import date


def voto(nascimento):
    x = date.today().year - nascimento
    return x


idade = voto(int(input('Digite seu ano de nascimento: ')))

if idade <= 16:
    print(f'Com {idade} anos: NÃO VOTA.')
if 17 <= idade <= 59:
    print(f'Com {idade} anos: VOTO OBRIGATÓRIO. ')
if idade >= 60:
    print(f'Com {idade} anos: VOTO OPCIONAL.')
