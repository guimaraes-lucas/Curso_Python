# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas
# as informações possíveis na tela.

x = input('Insira um valor: ')

print('Qual o tipo primitivo da variável?', type(x))
print('Só tem espaços? {}'.format(x.isspace()))
print('É um número? {}'.format(x.isnumeric()))
print('É alfabético? {}'.format(x.isalpha()))
print('É alfanumérico? {}'.format(x.isalnum()))
print('Esta em maiuscúlo? {}'.format(x.isupper()))
print('Está em minúsculo? {}'.format(x.islower()))
print('Está capitalizado? {}'.format(x.istitle()))


