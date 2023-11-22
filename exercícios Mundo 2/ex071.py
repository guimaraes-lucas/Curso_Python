"""
    Crie um programa que simula o funcionamento de um CAIXA ELETRÔNICO. No início, pergunte ao usuário qual será o VALOR
A SER SACADO (Número inteiro) e o programa vai informar quantas CÉDULAS de cada valor serão entregues.
    OBS:: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)

valor = int(input('Qual valor você quer sacar? R$ '))

cedula = 50
totalCedulas = 0

while True:
    if valor >= cedula:
        valor -= cedula
        totalCedulas += 1
    else:
        print(f'Total de {totalCedulas} cédulas de R$ {cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1

        totalCedulas = 0

        if valor == 0:
            break
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')