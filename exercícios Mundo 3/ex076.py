"""
    Crie um programa que tenha uma TUPLA única com NOMES DE PRODUTOS e seus respectivos PREÇOS, na sequência. No final,
mostre uma listagem de preços, organizando os dados de forma TABULAR.
"""


"""
produtos = ('Lápis', 'Borracha', 'Apontador', 'Estojo', 'Mochila', 'Cadernos', 'Canetas', 'Lápis de cor')
precos = (0.75, 0.50, 1.50, 5, 50, 12, 1, 12)

print('-'*20)
print('LISTAGEM DE PREÇOS')
print('-'*20)

contagem = 0
for p in produtos:
    print(produtos[0+contagem], end='')
    print('.'*20, end='')
    print(f'R$ {precos[0+contagem]}')
    contagem += 1
"""
listagem = ('Lápis', 0.75,
            'Borracha', 0.50,
            'Apontador', 1.50,
            'Estojo', 5,
            'Mochila', 50,
            'Cadernos', 12,
            'Canetas', 1,
            'Lápis de cor', 12)

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    if pos % 2 == 1:
        print(f'R$ {listagem[pos]:>}')