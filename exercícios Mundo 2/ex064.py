# Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. O programa só vai parar quando o usuário digitar o
# valor 999, que é a CONDIÇÃO DE PARADA. No final mostre QUANTOS NÚMEROS foram digitados e qual foi a SOMA entre eles.
# (Desconsiderando o FLAG)

num = int(input('Digite um número [999 para parar]: '))

contagem = total = 0

while num != 999:
    total += num
    contagem += 1
    num = int(input('Digite um número [999 para parar]: '))

print('Você digitou {} números e a soma deles é {}'.format(contagem, total))
