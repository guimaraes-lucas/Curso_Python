"""
    Crie um programa que leia NOME, SEXO e IDADE de VÁRIAS PESSOAS, guardando os dados de cada pessoa em um DICIONÁRIO e
todos os dicionários em uma LISTA. No final mostre:
        A) Quantas pessoas cadastradas      C) Uma lista com MULHERES
        B) A MÉDIA de idade                 D) Uma lista com IDADE acima da MÉDIA
"""
pessoa = {}
pessoas = []
soma = media = 0
while True:
    pessoa.clear()

    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('ERRO! Digite apenas M ou F')
    pessoa['idade'] = int(input('Idade: '))

    soma += pessoa['idade']
    pessoas.append(pessoa.copy())

    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if continuar in 'SN':
            break
        else:
            print('ERRO! Digite apenas S ou N')
    if continuar == 'N':
        break

print('=='*30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas')

media = soma / len(pessoas)
print(f'B) A média de idade é {media:5.2f}')

print(f'C) As mulheres cadastradas são: ', end='')
for item in pessoas:
    if item['sexo'] in 'Ff':
        print(f'{item["nome"]}', end=' ')
print()

print(f'D) Pessoas com idade acima da média: ', end='')
for item in pessoas:
    if item['idade'] > media:
        print(f'{item["nome"]}', end=' ')
