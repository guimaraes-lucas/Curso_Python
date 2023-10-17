# Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.

from time import sleep

for timer in range(10, -1, -1):
    print(timer)
    sleep(1)
print('BUM!   BUM!   POOOW!!')
