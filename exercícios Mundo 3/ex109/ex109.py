"""
    Modifique as funções que foram criadas no DESAFIO 107 para que elas aceitem UM PARÂMETRO a mais, informando se o
valor retornado por elas vai ser ou não formatado pela função MOEDA(), desenvolvida no DESAFIO 108.
"""
import moedas

valor = float(input('Digite o preço: R$  '))

print(f'A metade de {moedas.moeda(valor)} é {moedas.metade(valor, True)}')
print(f'O dobro de {moedas.moeda(valor)} é {moedas.dobro(valor, True)}')
print(f'Aumentando em 10%, temos {moedas.aumentar(valor, 10, True)}')
print(f'Diminuindo em 10%, temos {moedas.diminuir(valor, 10, True)}')

print()
valor1 = float(input('Digite o preço: R$  '))

print(f'A metade de {moedas.moeda(valor)} é {moedas.moeda(moedas.metade(valor))}')
print(f'O dobro de {moedas.moeda(valor)} é {moedas.moeda(moedas.dobro(valor))}')
print(f'Aumentando em 10%, temos {moedas.moeda(moedas.aumentar(valor, 10))}')
print(f'Diminuindo em 10%, temos {moedas.moeda(moedas.diminuir(valor, 10))}')
