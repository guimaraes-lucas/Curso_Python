"""
    Adapte o código do DESAFIO 107, criando uma função adicional chamada MOEDA() que consiga mostrar os valores como um
calor monetário formatado.

"""
import moedas

valor = float(input('Digite o preço: R$  '))

print(f'A metade de {moedas.moeda(valor)} é {moedas.moeda(moedas.metade(valor))}')
print(f'O dobro de {moedas.moeda(valor)} é {moedas.moeda(moedas.dobro(valor))}')
print(f'Aumentando em 10%, temos {moedas.moeda(moedas.aumentar(valor, 10))}')
print(f'Diminuindo em 10%, temos {moedas.moeda(moedas.diminuir(valor, 10))}')
