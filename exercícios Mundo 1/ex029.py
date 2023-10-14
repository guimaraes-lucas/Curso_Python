#  Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00 por cada KM acima do limite.

velocidade = int(input('Qual a velocidade do carro?: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você está acima da velocidade!!! Preste atenção !!!')
    print('Você irá pagar uma multa de R${},00'.format(multa))
else:
    print('Parabéns!!! Continue sua viajem em segurança')
