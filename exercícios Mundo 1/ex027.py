# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

nome = str(input('Insira seu nome completo: ')).strip()

div = nome.split()

pn = div[0]
un = div[len(div) - 1]

print('Olá, prazer em te conhecer')
print('Seu primeiro nome é: {}'.format(pn))
print('Seu último nome é: {}'.format(un))
