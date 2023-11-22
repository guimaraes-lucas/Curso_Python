"""
 Crie um programa que leia o NOME e o PREÇO de vários produtos. O programa deverá perguntar se o USUÁRIO vai continuar.
 No final, mostre:

    A) Qual é o TOTAL GASTO na compra.
    B) Quantos produtos custam maus de R$ 1000.
    C) Qual é o nome do produto MAIS barato.
"""
print('-'*30)
print('LOJAS SUPER BARATÃO')
print('-'*30)

maisBarato = ' '
total = maisDeMil = menorPreco = contagem = 0

while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$ '))

    contagem += 1
    total += preco

    if preco >= 1000:
        maisDeMil += 1

    if contagem == 1 or preco < menorPreco:
        menorPreco = preco
        maisBarato = produto

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break

print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {maisDeMil} produros custando mais de R$ 1000')
print(f'O produto mais barato foi {maisBarato} que custa R$ {menorPreco:.2f}')
