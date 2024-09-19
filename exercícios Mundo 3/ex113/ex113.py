"""
    Reescreva a função leiaInt() que fizemos no DESAFIO 104, incluindo agora a possibilidade da digitação de um número
de tipo válido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""
from utilidadesCeV import dados

num1 = dados.leiaInt('Digite um valor: ')
print(f'O valor digitado foi {num1}')

num2 = dados.leiaFloat('Digite outro valor: ')
print(f'O valor digitado foi {num2}')
