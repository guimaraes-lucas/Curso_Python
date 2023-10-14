# Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

c = float(input('Insira a temperatura em °C: '))
f = ((9 * c) + 160) / 5

print('Sua temperatura é {}°C, convertendo para Fahrenheit fica {}°F'.format(c, f))
