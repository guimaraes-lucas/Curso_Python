"""
    Crie um módulo chamado MOEDA.PY que tenha as funções incorporadas AUMENTAR(), DIMINUIR(), DOBRO() e METADE(). Faça
também um programa que IMPORTE esse módulo e use algumas dessas funções.
"""
from uteis import moedas

valor = float(input('Digite o preço: R$  '))

print(f'A metade de {valor} é {moedas.metade(valor)}')
print(f'O dobro de {valor} é {moedas.dobro(valor)}')
print(f'Aumentando em 10%, temos {moedas.aumentar(valor, 10)}')
print(f'Diminuindo em 10%, temos {moedas.diminuir(valor, 10)}')
