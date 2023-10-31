# Crie um programa que leia dois valores e mostre um MENU como o ao lado da tela: Seu programa deverá realizar a operação
# solicitada em cada caso.

from time import sleep

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
escolha = 0

while escolha != 5:

    print(' ')
    print('     [ 1 ] SOMAR')
    print('     [ 2 ] MULTIPLICAR')
    print('     [ 3 ] MAIOR')
    print('     [ 4 ] NOVOS NÚMEROS')
    print('     [ 5 ] SAIR DO PROGRAMA\n')

    escolha = int(input('>>>>> Qual é a sua opção?  '))
    print(' ')
    if escolha == 1:
        soma = num1 + num2
        print('{} + {} = {}'.format(num1, num2, soma))
    elif escolha == 2:
        mult = num1 * num2
        print('{} x {} = {}'.format(num1, num2, mult))
    elif escolha == 3:
        if num1 > num2:
            print('{} é maior'.format(num1))
        elif num1 < num2:
            print('{} é maior'.format(num2))
        elif num1 == num2:
            print('Ambos são iguais')
    elif escolha == 4:
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif escolha == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção inválida, tente novamente')

print('Programa finalizado, até logo!!')