"""
    Faça um programa que tenha uma FUNÇÃO chamada MAIOR(), que receba vários PARÂMETROS com valores inteiros. Seu
programa tem que analisar todos os valores e dizer qual deles é o MAIOR.
"""

def maior(* valores):
    maiorValor = 0

    if valores == 0:
        maiorValor = 0
    else:
        for x in valores:
            if x > maiorValor:
                maiorValor = x

    print('-=-'*30)
    print('Analisando os valores passados...')

    for x in valores:
        print(f'{x} ', end='')

    print(f'Foram informados {len(valores)} valores ao todo.')
    print(f'O maior valor informado foi {maiorValor}')
    print('-=-'*30)

maior(2,9,4,5,7,1)
maior(4,7,8)
maior(1,2)
maior(6)
maior()
