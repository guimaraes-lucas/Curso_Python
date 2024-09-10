"""
    Crie um PACOTE chamado utilidadesCeV que tenha dois MÓDULOS INTERNOS chamados MOEDA e DADO.
    Transfira todas as funções utilizadas nos DESAFIOS 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando
"""

from utilidadesCeV import moeda

valor = float(input('Digite o preço: R$  '))

moeda.resumo(valor, 80, 20)
