# Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZÃO de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão.

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Qual a razão?: '))
enesimo = termo + (10 - 1) * razao

for progressao in range(termo, enesimo + razao, razao):
    print('{}'.format(progressao), end=' → ')
print('ACABOU')
