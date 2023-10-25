"""
Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 pessoas. No final do programa, mostre:

=> A média de idade do grupo.               => Quantas mulheres têm menos de 20 anos
=> Qual é o nome do homem mais velha.
"""
idadeTotal = 0
maisVelho = 0
nomeVelho = ''
mulher20 = 0

for obj in range(1, 5):

    print('------{}° PESSOA------'.format(obj))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))

    idadeTotal += idade

    if obj == 1 and sexo in 'Mm':
        maisVelho = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maisVelho:
        maisVelho = idade
        nomeVelho = nome

    if sexo in 'Ff' and idade < 20:
        mulher20 += 1

media = idadeTotal / 4


print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho possui {} anos e se chama {}'.format(maisVelho, nomeVelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher20))
