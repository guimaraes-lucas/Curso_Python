"""
Crie um programa que leia a IDADE e o SEXO de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
o USUÁRIO quer ou não continuar. No final, mostre:

    A) Quantas pessoas têm mais de 18 anos
    B) Quantos HOMENS foram cadastrados.
    C) Quantas MULHERES têm menos de 20 ANOS.
"""


while True:
    contagem = homens = mulheres = 0
    sexo = ' '
    continuar = ' '

    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)

    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()

    if idade >= 18:
        contagem += 1

    if sexo == 'M':
        homens += 1

    if sexo == 'F':
        if idade < 20:
            mulheres += 1

    print('-' * 20)
    
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()

    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {contagem}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')
