# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta
# necessária para pintá-la. Sabendo que cada litro de tinta , pinta uma área de 2m².

lg = float(input('Qual a largura de sua parede?: '))
at = float(input('Qual a altura de sua parede?: '))

ar = lg * at
t = ar / 2

print('As dimensões da sua parede são {}m x {}m, a área total dela é {}m²'.format(lg, at, ar))
print('Serão necessários {}L de tinta'.format(t))

