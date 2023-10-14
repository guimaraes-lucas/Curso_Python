# Crie um programa que leia o nome completo de uma pessoa e mostre:
#       => O nome com todas as letras maiúsculas e minúsculas.
#       => Quantas letras no total (sem considerar espaços).
#       => Quantas letras tem o primeiro nome.

nome = str(input('Qual o seu nome completo?: ')).strip()

print('O seu nome em maiúscula é {}'.format(nome.upper()))
print('O seu nome em minúscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome possui {} letras'.format(nome.find(' ')))
