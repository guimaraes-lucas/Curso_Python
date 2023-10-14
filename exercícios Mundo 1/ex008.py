# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

x = float(input('Insira uma distância em metros: '))

km  = x / 1000
hm  = x / 100
dam = x / 10
dm  = x * 10
cm  = x * 100
mm  = x * 1000

print('A medida de {}m corresponde a: \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'.format(x, km, hm, dam, dm, cm, mm))
